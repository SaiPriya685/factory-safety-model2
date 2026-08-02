from fastapi import APIRouter

from backend.services.result_store import result_store


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/live")
def live_analysis():

    return result_store.get()