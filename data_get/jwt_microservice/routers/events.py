import os
from fastapi import APIRouter
from utils import data_fetcher

# Initialize the APIRouter
router = APIRouter(
    tags=["Events"],
)

# --- Configuration ---
# Use os.environ[] to raise an error if critical config is missing
try:
    JWT_SUBJECT = os.environ["JWT_SUBJECT_EVENTS"]
    WIX_ENDPOINT = os.environ["WIX_EVENTS_ENDPOINT"]
except KeyError as e:
    raise RuntimeError(f"Missing required environment variable: {e}")

LOCAL_PATH = "wix_events_data.json"
DATA_TYPE = "Events"


# --- Call the Data Fetcher Utility ---
@router.get("/events")
async def download_events():
    """
    Calls the generalized data fetch utility for Events data.
    """

    return await data_fetcher(
        jwt_subject=JWT_SUBJECT,
        wix_endpoint=WIX_ENDPOINT,
        local_path=LOCAL_PATH,
        data_type=DATA_TYPE,
    )
