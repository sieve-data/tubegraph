from typing import Literal

import requests
import sieve
from create_graph import create_graph
from get_channel_vids import get_channel_id


def url_exists_on_tubegraph(slug: str, *, timeout: float = 5.0) -> bool:
    base = "https://tubegraph.vercel.app/"
    url = f"{base}{slug.lstrip('/')}"  # ensure no leading slash duplication

    try:
        # Use HEAD for speed; fall back to GET if HEAD not allowed
        resp = requests.head(url, allow_redirects=True, timeout=timeout)
        if resp.status_code == 405:  # Method Not Allowed – server wants GET
            resp = requests.get(url, allow_redirects=True, timeout=timeout)

        print(resp)
        return resp.status_code != 404

    except (requests.RequestException, requests.Timeout):
        # Network error, DNS failure, etc.  Treat as "does not exist".
        return False


@sieve.function(
    name="create-tubegraph-pages",
    python_version="3.10",
    python_packages=[
        "openai",
        "python-dotenv",
        "sievedata",
        "webvtt-py",
        "isodate",
        "google-api-python-client",
        "PyGithub",
        "numpy",
    ],
)
def get_items(
    username: str,
    min_vid_duration: int,
    sort_by: Literal["views", "upload_date"],
):
    username = username.replace("@", "").lower()
    channel_id = get_channel_id(username)
    if channel_id is None:
        return {"result": "Channel Invalid!"}
    print("getting, ", channel_id)
    output = create_graph(
        username=username,
        channel_id=channel_id,
        min_vid_duration=min_vid_duration,
        sort_by=sort_by,
    )
    print(output)
    return {
        "result": f"May take 1-2 minutes to load here: <a href='https://tubegraph.vercel.app/{username}/{username}'>here.</a>"
    }


# print(get_items("MysteryOre", 20, "views"))
