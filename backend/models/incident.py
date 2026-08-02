from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from backend.database import Base


class Incident(Base):

    __tablename__ = "incidents"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    violation = Column(
        String
    )


    severity = Column(
        String
    )


    location = Column(
        String
    )


    evidence_path = Column(
        String,
        nullable=True
    )


    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )