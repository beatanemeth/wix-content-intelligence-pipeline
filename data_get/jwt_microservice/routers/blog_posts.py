import os
from fastapi import APIRouter
from utils import data_fetcher

# Initialize the APIRouter
router = APIRouter(
    tags=["Posts"],
)

# ---Configuration ---
# Use os.environ[] to raise an error if critical config is missing
try:
    JWT_SUBJECT = os.environ["JWT_SUBJECT_POSTS"]
    WIX_ENDPOINT = os.environ["WIX_POSTS_ENDPOINT"]
except KeyError as e:
    raise RuntimeError(f"Missing required environment variable: {e}")

LOCAL_PATH = "wix_blog_posts_data.json"
DATA_TYPE = "Posts"


# --- Call the Data Fetcher Utility ---
@router.get("/blog/posts")
async def download_blog_posts():
    """
    Calls the generalized data fetch utility for Blog Posts data.
    """

    return await data_fetcher(
        jwt_subject=JWT_SUBJECT,
        wix_endpoint=WIX_ENDPOINT,
        local_path=LOCAL_PATH,
        data_type=DATA_TYPE,
    )
