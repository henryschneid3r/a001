from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health():
    return {"message": "The system looks healthy..."}
