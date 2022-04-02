from redis_om import HashModel

from ..services.redis import client as redis


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis