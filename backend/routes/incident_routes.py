from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from backend.database import get_db

from backend.models.incident import Incident


router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)



def format_incident(incident):

    return {

        "id": incident.id,

        "violation": incident.violation,

        "severity": incident.severity,

        "location": incident.location,

        "created_at": incident.created_at,

        "evidence_path": incident.evidence_path

    }



@router.get("/")
def get_incidents(
    db: Session = Depends(get_db)
):

    incidents = db.query(
        Incident
    ).order_by(
        Incident.created_at.desc()
    ).all()


    return [
        format_incident(item)
        for item in incidents
    ]



@router.get("/latest")
def latest_incidents(
    db: Session = Depends(get_db)
):

    incidents = db.query(
        Incident
    ).order_by(
        Incident.created_at.desc()
    ).limit(5).all()


    return [
        format_incident(item)
        for item in incidents
    ]