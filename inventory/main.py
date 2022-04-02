from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .services.redis import init_redis_client
from .routes import product, home

app = FastAPI(
    terms_of_service="https://www.termsfeed.com/blog/sample-terms-of-service-template/",
    license_info="",
    contact=dict(
        name="Bolaji O.",
        email="25608335+BolajiOlajide@users.noreply.github.com",
    ),
    version="0.0.0",
    description="Sample Inventory Microservice"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['POST', 'GET', 'OPTIONS', 'DELETE'],
    allow_headers=['*']
)
app.include_router(home.router)
app.include_router(product.router)

# initialize redis client
init_redis_client()
