"""
Fetch every public video on a given YouTube channel.

Usage:
    python get_channel_videos.py UC_x5XG1OV2P6uZZ5FSM9Ttw
"""

import os
import sys

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")  # set in your shell
CHANNEL_ID = sys.argv[1] if len(sys.argv) > 1 else None
if not CHANNEL_ID:
    sys.exit("Pass the channel ID (or set CHANNEL_ID in code).")


def get_uploads_playlist_id(youtube, channel_id: str) -> str:
    """Return the channel’s ‘uploads’ playlist ID."""
    resp = (
        youtube.channels()
        .list(part="contentDetails", id=channel_id, maxResults=1)
        .execute()
    )

    items = resp.get("items")
    if not items:
        raise ValueError(f"Channel {channel_id} not found")

    return items[0]["contentDetails"]["relatedPlaylists"]["uploads"]


def get_all_videos(youtube, playlist_id: str) -> list[dict]:
    """Return a list of dicts with videoId, title, and publishedAt."""
    vids, page_token = [], None
    while True:
        resp = (
            youtube.playlistItems()
            .list(
                part="snippet,contentDetails",
                playlistId=playlist_id,
                maxResults=50,
                pageToken=page_token,
            )
            .execute()
        )

        for it in resp["items"]:
            vids.append(
                {
                    "videoId": it["contentDetails"]["videoId"],
                    "title": it["snippet"]["title"],
                    "publishedAt": it["contentDetails"]["videoPublishedAt"],
                }
            )

        page_token = resp.get("nextPageToken")
        if not page_token:  # no more pages
            break
    return vids


def main():
    youtube = build("youtube", "v3", developerKey=API_KEY)

    uploads_pid = get_uploads_playlist_id(youtube, CHANNEL_ID)
    videos = get_all_videos(youtube, uploads_pid)

    print(f"{len(videos)} videos found on channel {CHANNEL_ID}\n")
    for v in videos:
        url = f"https://www.youtube.com/watch?v={v['videoId']}"
        print(f"{v['publishedAt']}  {v['title']}  {url}")


if __name__ == "__main__":
    main()
