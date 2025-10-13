from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import logging
from pathlib import Path

# Import route modules
from routes import personal, experience, projects, skills, achievements, education, contact
from database import close_db_connection

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Create the main app
app = FastAPI(title="Portfolio API", description="API for Shreya's Portfolio Website", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a router with the /api prefix for the root endpoint
api_router = APIRouter(prefix="/api")

@api_router.get("/")
async def root():
    return {"message": "Portfolio API is running successfully!", "version": "1.0.0"}

# Include all route modules
app.include_router(personal.router)
app.include_router(experience.router)
app.include_router(projects.router)
app.include_router(skills.router)
app.include_router(achievements.router)
app.include_router(education.router)
app.include_router(contact.router)

# Include the root router
app.include_router(api_router)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup_event():
    logger.info("Portfolio API is starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Portfolio API is shutting down...")
    await close_db_connection()

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "portfolio-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)