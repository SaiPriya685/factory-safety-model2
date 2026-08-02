import os
import cv2
from datetime import datetime


EVIDENCE_PATH = "evidence/images"


os.makedirs(
    EVIDENCE_PATH,
    exist_ok=True
)



def save_frame(frame):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


    filename = (
        f"incident_{timestamp}.jpg"
    )


    filepath = os.path.join(
        EVIDENCE_PATH,
        filename
    )


    cv2.imwrite(
        filepath,
        frame
    )


    return filepath