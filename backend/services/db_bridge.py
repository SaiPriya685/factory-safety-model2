from backend.database import SessionLocal
from backend.services.incident_service import save_incident


def store_incident(alert, analysis):

    db = SessionLocal()

    try:

        save_incident(
            db,
            alert,
            analysis
        )

    finally:

        db.close()