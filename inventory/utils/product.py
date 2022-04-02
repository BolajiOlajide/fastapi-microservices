from ..models.product import Product


def format_product(pk: str):
    product = Product.get(pk)

    return dict(
        id=product.pk,
        name=product.name,
        price=product.price,
        quantity=product.quantity
    )
