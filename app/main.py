from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Backend API for AI-Based Legal Contract Analysis and Risk Detection System",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}
