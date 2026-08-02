from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.incident import Incident


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/stats")
def dashboard_stats(
    db: Session = Depends(get_db)
):

    # Total incidents

    total = db.query(
        Incident
    ).count()


    # Critical incidents

    critical = db.query(
        Incident
    ).filter(
        Incident.severity == "CRITICAL"
    ).count()


    # High risk incidents

    high = db.query(
        Incident
    ).filter(
        Incident.severity == "HIGH"
    ).count()


    # Fire events

    fire_events = db.query(
        Incident
    ).filter(
        Incident.violation == "Fire Detected"
    ).count()


    # Helmet violations

    helmet_events = db.query(
        Incident
    ).filter(
        Incident.violation == "Missing Helmet"
    ).count()



    # -------------------------------
    # Safety Score Calculation
    # Based on last 24 hours only
    # -------------------------------

    recent_time = datetime.utcnow() - timedelta(hours=24)


    recent_incidents = db.query(
        Incident
    ).filter(
        Incident.created_at >= recent_time
    ).all()



    recent_critical = sum(
        1
        for incident in recent_incidents
        if incident.severity == "CRITICAL"
    )


    recent_high = sum(
        1
        for incident in recent_incidents
        if incident.severity == "HIGH"
    )



    # Penalty calculation

    # Normalized Safety Score

    # Improved Safety Score Calculation

    penalty = (
    recent_critical * 0.02
    +
    recent_high * 0.01
    )


    safety_score = round(
    max(0, 100 - penalty)
    )   



    return {

        "total_incidents": total,

        "critical_events": critical,

        "high_risk_events": high,

        "fire_events": fire_events,

        "helmet_violations": helmet_events,

        "safety_score": safety_score,

        "recent_incidents": len(recent_incidents)

    }