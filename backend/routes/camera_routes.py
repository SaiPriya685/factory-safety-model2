from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from backend.services.ai_service import ai_service
from backend.services.video_stream import generate_frames



router = APIRouter(
    prefix="/camera",
    tags=["Camera"]
)



@router.post("/start")
def start_camera():

    return ai_service.start()



@router.post("/stop")
def stop_camera():

    return ai_service.stop()



@router.get("/status")
def camera_status():

    return ai_service.status()



@router.get("/video")
def video_feed():

    return StreamingResponse(
        generate_frames(),
        media_type=
        "multipart/x-mixed-replace; boundary=frame"
    )