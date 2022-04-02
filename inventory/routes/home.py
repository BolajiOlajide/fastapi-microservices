from fastapi import APIRouter, Depends

from ..dependencies import get_token_header


router = APIRouter(
    prefix="",
    tags=["home"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return {"message": "Hello inventory World"}