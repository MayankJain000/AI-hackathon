import uvicorn
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file if present
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Make sure required environment variables are set or use the provided one
gemini_api_key = "AIzaSyD2sEVrBWFCBRkp9jaFhAWUDKPm3A-fPMA"
if not gemini_api_key:
    logger.warning(
        "GEMINI_API_KEY environment variable not set and no default key provided. "
        "Some functionality will be limited to fallback responses."
    )

def start():
    """Run the API server."""
    logger.info("Starting Emotional Productivity Assistant API with Google Gemini")
    
    # Get port from environment or use default
    port = int(os.getenv("PORT", 8000))
    
    # Run the FastAPI app with uvicorn
    uvicorn.run(
        "app.api.main:app",
        host="0.0.0.0",
        port=port,
        reload=True,
    )

if __name__ == "__main__":
    start() 