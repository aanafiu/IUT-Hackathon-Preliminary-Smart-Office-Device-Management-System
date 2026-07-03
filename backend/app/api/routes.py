from fastapi import APIRouter
from app.core.state import manager

router = APIRouter()


@router.get("/devices")
def get_devices():
    return manager.get_all_devices()