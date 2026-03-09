def determine_primary_category(cats):
    """
    In cases where a blog post has multiple categories, we need a consistent way to determine the primary category for analysis.
    Handle following cases:
    - if contains #Vendégblog take this as a primary category
    - if contains #ManóDuma take this as a primary category
    - in other cases: take the first category in the list (Default)

    Args:
        cats (list): A list of category strings.

    Returns:
        str: The selected primary category.
    """

    CAT_GUEST_BLOG = "#Vendégblog"
    CAT_SERIES = "#ManóDuma"

    # 1. Handle empty or non-list inputs safely
    if not cats or not isinstance(cats, list):
        return "Uncategorized"

    # 2. Case: contains #Vendégblog
    if CAT_GUEST_BLOG in cats:
        return CAT_GUEST_BLOG

    # 3. Case: contains #ManóDuma
    if CAT_SERIES in cats:
        return CAT_SERIES

    # 4. Default: Take the first category in the list
    return cats[0]
