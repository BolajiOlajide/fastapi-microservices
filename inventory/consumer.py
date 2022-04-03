import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

import time

from inventory.services.redis import init_redis_client
from inventory.models.product import Product


key = "order_completed"
group = "inventory-group"
redis = init_redis_client( )

try:
    redis.xgroup_create(key, group)
except:
    print("Group already exists!")

while True:
    try:
        results = redis.xreadgroup(group, key, {key: ">"}, None)

        if results != []:
            for result in results:
                obj = result[1][0][1]
                product = Product.get(obj["product_id"])
                print(product)

                new_quantity = product.quantity - int(obj["quantity"])

                if new_quantity > 0:
                    product.quantity = new_quantity
                else:
                    product.status = "failed"
                product.save()
    except Exception as e:
        print(str(e))

    # consume messages every second
    time.sleep(1)