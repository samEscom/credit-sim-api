from fastapi import APIRouter

from app.api.schemas.response import HealthResponse

router = APIRouter(
    prefix="/health",
    tags=["health"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def api_check():
    return HealthResponse(status="ok")
