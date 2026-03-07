import os
from fastapi import APIRouter, HTTPException
from utils import data_fetcher

# Initialize the APIRouter
router = APIRouter(
    tags=["Collections"],
)

# --- Configuration ---
# Use os.environ[] to raise an error if critical config is missing
try:
    JWT_SUBJECT = os.environ["JWT_SUBJECT_COLLECTIONS"]
    WIX_ENDPOINT = os.environ["WIX_COLLECTIONS_ENDPOINT"]
except KeyError as e:
    raise RuntimeError(f"Missing required environment variable: {e}")

LOCAL_PATH_ARTICLES = "wix_articles_data.json"
LOCAL_PATH_ARTICLES_CATEGORY = "wix_articles-category_data.json"

COLLECTION_MAP = {
    "articles": LOCAL_PATH_ARTICLES,
    "articles-category": LOCAL_PATH_ARTICLES_CATEGORY,
}


# --- Call the Data Fetcher Utility ---
@router.get("/collections/{collection}")
async def download_collections_(collection: str):
    """
    Determines which collection to fetch based on the URL path.
    """

    # Validation check
    if collection not in COLLECTION_MAP:
        raise HTTPException(status_code=400, detail="Invalid collection type")

    local_path = COLLECTION_MAP[collection]

    # Functional logic
    return await data_fetcher(
        jwt_subject=JWT_SUBJECT,
        wix_endpoint=f"{WIX_ENDPOINT}?coll={collection}",
        local_path=local_path,
        data_type=collection.capitalize(),
    )
