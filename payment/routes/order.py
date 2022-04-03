import time

from fastapi import APIRouter, Depends, BackgroundTasks
from starlette.requests import Request
import requests

from ..dependencies import get_token_header
from ..models.order import Order
from ..services.redis import init_redis_client


router = APIRouter(
    prefix="/order",
    tags=["order"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/{pk}")
async def fetch_order(pk: str):
    return Order.get(pk)

@router.post("/")
async def create_order(request: Request, background_tasks: BackgroundTasks): # product_id, quantity
    x_token = request.headers["x-token"]
    body = await request.json()

    product_id = body["product_id"]
    inventory_url = f"http://localhost:8081/product/{product_id}"

    req = requests.get(inventory_url, headers={
        "x-token": x_token
    })

    product = req.json()
    order = Order(
        product_id=product_id,
        price=product["price"],

        # the fee is always 20% of the product price
        fee= 0.2 * product["price"],

        # total is evaluated as `price + fee`
        total=1.2*product["price"],

        quantity=body["quantity"],
        status="pending"
    )
    order.save()
    background_tasks.add_task(order_completed, order)

    return order

def order_completed(order: Order):
    # sleep for 5s to simulate a long running process
    time.sleep(5)

    order.status = "completed"
    order.save()

    # sending to redis stream
    redis = init_redis_client()
    redis.xadd("order_completed", order.dict(), "*") # the * tells redis to use an auto generated ID

    print("done sending order to redis stream...")
