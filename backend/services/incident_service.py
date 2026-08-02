from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from backend.models.incident import Incident



def save_incident(
        db: Session,
        alert,
        analysis
):


    for violation in analysis["violations"]:


        violation_type = violation["type"]


        severity = violation["severity"]



        # Check duplicate within last 30 seconds

        recent_time = (
            datetime.utcnow()
            -
            timedelta(seconds=30)
        )


        existing = db.query(
            Incident
        ).filter(

            Incident.violation == violation_type,

            Incident.created_at >= recent_time

        ).first()



        if existing:

            continue



        incident = Incident(

            violation=violation_type,

            severity=severity,

            location="Factory Floor"

        )


        db.add(incident)



    db.commit()