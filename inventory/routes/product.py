from fastapi import APIRouter, Depends

from ..dependencies import get_token_header
from ..models.product import Product
from ..utils.product import format_product


router = APIRouter(
    prefix="/product",
    tags=["product"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def fetch_all_products():
    return [format_product(pk) for pk in Product.all_pks()]

@router.post("/")
def create_product(product: Product):
    return product.save()

@router.get("/{pk}")
def fetch_single_product(pk: str):
    return format_product(pk)

@router.delete("/{pk}")
def delete_product(pk: str):
    return Product.delete(pk)