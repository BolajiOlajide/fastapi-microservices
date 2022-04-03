from fastapi import APIRouter


router = APIRouter(
    prefix="",
    tags=["home"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return {"message": "Hello payment World"}