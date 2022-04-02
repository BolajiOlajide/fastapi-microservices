from redis_om import get_redis_connection


client = None

def init_redis_client():
    global client
    if client == None:
        client = get_redis_connection(
            host="redis-13381.c263.us-east-1-2.ec2.cloud.redislabs.com",
            port="13381",
            # I'd have taken down this instance by the time you see this code lol.
            password="arYjB9xFRksd42aua39cXi3DvOTbGcwB",
            decode_responses=True
        )
    return client
