from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.incident import Incident

from backend.services.report_generator import generate_incident_report



router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)



@router.get("/{incident_id}")
def download_report(
    incident_id:int,
    db:Session = Depends(get_db)
):


    incident = db.query(
        Incident
    ).filter(
        Incident.id == incident_id
    ).first()



    if not incident:

        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )


    filepath = generate_incident_report(
        incident
    )


    return FileResponse(
        filepath,
        media_type="application/pdf",
        filename=f"incident_{incident_id}.pdf"
    )