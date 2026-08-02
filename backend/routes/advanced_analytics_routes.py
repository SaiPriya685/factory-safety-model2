from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.incident import Incident


router = APIRouter(
    prefix="/advanced",
    tags=["Advanced Analytics"]
)



@router.get("/summary")
def analytics_summary(
    db: Session = Depends(get_db)
):

    incidents = db.query(
        Incident
    ).all()


    violation_count = {}


    severity_count = {}


    for item in incidents:

        violation_count[item.violation] = (
            violation_count.get(item.violation,0)
            + 1
        )


        severity_count[item.severity] = (
            severity_count.get(item.severity,0)
            + 1
        )


    return {

        "total": len(incidents),

        "violations": violation_count,

        "severity": severity_count

    }