from ai.utils.camera import CameraManager
from ai.detection.ppe_detector import PPEDetector
from ai.analytics.safety_analyzer import SafetyAnalyzer
from ai.analytics.risk_engine import RiskEngine
from ai.alerts.alert_manager import AlertManager
from ai.outputs.incident_logger import IncidentLogger
from ai.report.response_formatter import format_ai_response

from backend.services.frame_store import frame_store
from backend.services.result_store import result_store
from backend.services.db_bridge import store_incident
from backend.services.evidence_manager import save_frame

import cv2
def main(stop_event=None):

    camera = CameraManager()

    detector = PPEDetector()

    analyzer = SafetyAnalyzer()

    risk_engine = RiskEngine()

    alert_manager = AlertManager()

    incident_logger = IncidentLogger()

    try:

        while True:

            # Stop immediately if requested
            if stop_event and stop_event.is_set():
                print("Stopping AI loop...")
                break

            frame = camera.read()

            if frame is None:
                break

            # Check again after reading frame
            if stop_event and stop_event.is_set():
                break

            # Detect objects
            results, detections = detector.detect(frame)

            if stop_event and stop_event.is_set():
                break

            # Analyze safety
            analysis = analyzer.analyze(detections)

            if stop_event and stop_event.is_set():
                break

            print("\nDetections:")
            for item in analysis["detections"]:
                print(item)

            print("\nViolations:")
            for item in analysis["violations"]:
                print(item)

            ai_response = format_ai_response(
                analysis["violations"]
            )

            print("\nAI Response:")
            print(ai_response)

            risk = risk_engine.calculate(
                analysis
            )

            if stop_event and stop_event.is_set():
                break

            alert = alert_manager.generate_alert(
                risk
            )

            result_store.update({
                "risk_level": risk["risk_level"],
                "violations": analysis["violations"],
                "detections": analysis["detections"],
                "alert": alert
            })

            # Save incident only if monitoring is still active
            if not (stop_event and stop_event.is_set()):

                if risk["risk_level"] != "LOW":

                    evidence_path = save_frame(frame)

                    incident_logger.save(
                        alert,
                        analysis
                    )

                    store_incident(
                        alert,
                        analysis,
                    )

            if stop_event and stop_event.is_set():
                break

            frame = detector.draw(
                frame,
                results
            )

            cv2.putText(
                frame,
                f"Risk: {risk['risk_level']}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

            frame_store.update(frame)

            print("Frame sent to dashboard")

    finally:

        camera.release()

        print("Camera released.")