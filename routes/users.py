from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_users():
    # TODO: DB-Abfrage über repos/
    return []