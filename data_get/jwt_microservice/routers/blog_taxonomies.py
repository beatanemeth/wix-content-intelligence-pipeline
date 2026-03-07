import os
from fastapi import APIRouter, HTTPException
from utils import data_fetcher

# Initialize the APIRouter
router = APIRouter(
    tags=["Taxonomies"],
)

# --- Configuration ---
# Use os.environ[] to raise an error if critical config is missing
try:
    JWT_SUBJECT = os.environ["JWT_SUBJECT_BLOG_TAXONOMIES"]
    WIX_ENDPOINT = os.environ["WIX_BLOG_TAXONOMIES_ENDPOINT"]
except KeyError as e:
    raise RuntimeError(f"Missing required environment variable: {e}")

LOCAL_PATH_CATEGORIES = "wix_blog_categories_data.json"
LOCAL_PATH_TAGS = "wix_blog_tags_data.json"

TAXONOMY_MAP = {"categories": LOCAL_PATH_CATEGORIES, "tags": LOCAL_PATH_TAGS}


# --- Call the Data Fetcher Utility ---
@router.get("/blog/{taxonomy_type}")
async def download_blog_taxonomies_(taxonomy_type: str):
    """
    Determines to fetch blog taxonomies based on the URL path.
    """

    # Validation check
    if taxonomy_type not in TAXONOMY_MAP:
        raise HTTPException(status_code=400, detail="Invalid taxonomy type")

    local_path = TAXONOMY_MAP[taxonomy_type]

    # Functional logic
    return await data_fetcher(
        jwt_subject=JWT_SUBJECT,
        wix_endpoint=f"{WIX_ENDPOINT}?tax={taxonomy_type}",
        local_path=local_path,
        data_type=taxonomy_type.capitalize(),
    )
