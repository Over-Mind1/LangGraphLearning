from langchain.tools import tool
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools.ddg_search import DuckDuckGoSearchRun


# =========================
# DuckDuckGo Search Tool
# =========================

ddg_api_wrapper = DuckDuckGoSearchAPIWrapper(
    max_results=2,
    source="text"
)

@tool("ddg_search")
def ddg_search(query: str) -> str:
    """
    Search DuckDuckGo and return relevant results.
    """
    ddg = DuckDuckGoSearchRun(
        api_wrapper=ddg_api_wrapper
    )

    return ddg.invoke(query)


# =========================
# User Data Tool
# =========================

USERS_DB = {
    "1": {
        "name": "Ahmed",
        "age": 28,
        "role": "Developer",
        "email": "ahmed@example.com"
    },
    "2": {
        "name": "Sara",
        "age": 24,
        "role": "Designer",
        "email": "sara@example.com"
    },
    "3": {
        "name": "Omar",
        "age": 35,
        "role": "Manager",
        "email": "omar@example.com"
    }
}


@tool("get_user_data")
def get_user_data(user_id: str) -> str:
    """
    Retrieve user data using a user ID.
    """

    user = USERS_DB.get(user_id)

    if user:
        return str(user)

    return f"User with ID {user_id} not found."