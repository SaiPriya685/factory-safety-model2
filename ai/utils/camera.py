"""
camera.py

Camera manager for AI Factory Safety Copilot.
"""

import cv2
import time

from ai.utils.config import (
    CAMERA_ID,
    FRAME_WIDTH,
    FRAME_HEIGHT,
)

from ai.utils.logger import Logger


logger = Logger.get_logger("Camera")


class CameraManager:

    def __init__(self):

        self.cap = cv2.VideoCapture(CAMERA_ID)

        if not self.cap.isOpened():
            logger.error("Unable to open camera.")
            raise RuntimeError("Camera not found.")

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

        self.previous_time = time.time()

        logger.info("Camera initialized successfully.")

    
    def read(self):

        if self.cap is None:
            return None

        success, frame = self.cap.read()

        if not success:
            return None

        return frame

    def calculate_fps(self):

        current_time = time.time()
        fps = 1 / (current_time - self.previous_time)
        self.previous_time = current_time

        return int(fps)
    
    
    def release(self):

        if self.cap is not None and self.cap.isOpened():
            self.cap.release()
            self.cap = None
            logger.info("Camera released.")