from redis_om import get_redis_connection


client = None

def init_redis_client():
    global client
    if client == None:
        client = get_redis_connection(
            host="localhost",
            port="6379",
            password="",
            decode_responses=True
        )
    return client
