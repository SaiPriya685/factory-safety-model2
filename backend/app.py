from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from backend.config import settings
from backend.database import Base, engine

from backend.models import user
from backend.models import incident
from backend.routes.camera_routes import router as camera_router
from backend.routes.health_routes import router as health_router
from backend.routes.auth_routes import router as auth_router
from backend.routes.analytics_routes import router as analytics_router
from backend.routes.incident_routes import router as incident_router
from backend.routes.dashboard_routes import router as dashboard_router
from backend.routes.advanced_analytics_routes import router as advanced_router
from backend.routes.report_routes import router as report_router
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
    ],

    allow_credentials=True,

    allow_methods=[
        "*"
    ],

    allow_headers=[
        "*"
    ],
)
app.mount(
    "/evidence",
    StaticFiles(directory="evidence"),
    name="evidence"
)
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(camera_router)
app.include_router(analytics_router)
app.include_router(incident_router)
app.include_router(dashboard_router)
app.include_router(
    advanced_router
)
app.include_router(
    report_router
)
@app.get("/")
def root():
    return {"message": "Backend Running"}