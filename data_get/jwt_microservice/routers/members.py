import os
from fastapi import APIRouter
from utils import data_fetcher

# Initialize the APIRouter
router = APIRouter(
    tags=["Members"],
)

# ---Configuration ---
# Use os.environ[] to raise an error if critical config is missing
try:
    JWT_SUBJECT = os.environ["JWT_SUBJECT_MEMBERS"]
    WIX_ENDPOINT = os.environ["WIX_MEMBERS_ENDPOINT"]
except KeyError as e:
    raise RuntimeError(f"Missing required environment variable: {e}")

LOCAL_PATH = "wix_members_data.json"
DATA_TYPE = "Members"


# --- Call the Data Fetcher Utility ---
@router.get("/members")
async def download_members():
    """
    Calls the generalized data fetch utility for Members data.
    """

    return await data_fetcher(
        jwt_subject=JWT_SUBJECT,
        wix_endpoint=WIX_ENDPOINT,
        local_path=LOCAL_PATH,
        data_type=DATA_TYPE,
    )
