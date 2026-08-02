"""
ppe_detector.py

Detects worker PPE compliance.
"""

from ultralytics import YOLO

from ai.utils.logger import Logger

from ai.utils.config import (
    SAFETY_MODEL,
    CONFIDENCE_THRESHOLD
)

from ai.detection.classes import SAFETY_CLASSES



class PPEDetector:


    def __init__(self):

        self.logger = Logger.get_logger(
            "PPEDetector"
        )


        self.logger.info(
            "Loading PPE detection model..."
        )


        self.model = YOLO(
            SAFETY_MODEL
        )


        self.logger.info(
            "PPE detector initialized."
        )



    def detect(self, frame):


        results = self.model(
            frame,

            conf=max(
                CONFIDENCE_THRESHOLD,
                0.65
            ),

            iou=0.45,

            max_det=20,

            verbose=False
        )


        detections = []


        for result in results:


            seen = {}


            for box in result.boxes:


                class_id = int(
                    box.cls[0]
                )


                confidence = float(
                    box.conf[0]
                )


                class_name = SAFETY_CLASSES.get(
                    class_id,
                    "unknown"
                )


                # keep highest confidence detection
                if class_name in seen:

                    if confidence > seen[class_name]["confidence"]:

                        seen[class_name] = {

                            "class_id": class_id,

                            "name": class_name,

                            "confidence": round(
                                confidence,
                                3
                            )
                        }


                else:

                    seen[class_name] = {

                        "class_id": class_id,

                        "name": class_name,

                        "confidence": round(
                            confidence,
                            3
                        )
                    }



            detections.extend(
                seen.values()
            )



        return results, detections



    def draw(
        self,
        frame,
        results
    ):


        annotated = results[0].plot()


        return annotated