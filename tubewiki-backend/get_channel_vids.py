"""
Fetch every public video on a given YouTube channel.

Usage:
    python get_channel_videos.py UC_x5XG1OV2P6uZZ5FSM9Ttw
"""

import os
from datetime import datetime
from typing import List, Literal

import isodate
import requests
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")  # set in your shell


def get_channel_id(handle):
    query = handle.lstrip("@")
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {"part": "snippet", "q": query, "type": "channel", "key": API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    for item in data.get("items", []):
        if item["snippet"]["channelTitle"].lower().replace(" ", "") == query.lower():
            return item["snippet"]["channelId"]
    return None


def get_uploads_playlist_id(youtube, channel_id: str) -> str:
    """Return the channel's 'uploads' playlist ID."""
    resp = (
        youtube.channels()
        .list(part="contentDetails", id=channel_id, maxResults=1)
        .execute()
    )

    items = resp.get("items")
    if not items:
        raise ValueError(f"Channel {channel_id} not found")

    return items[0]["contentDetails"]["relatedPlaylists"]["uploads"]


def get_video_details(youtube, video_ids: List[str]) -> dict:
    """Fetch duration and view count for a list of video IDs."""
    details = {}
    for i in range(0, len(video_ids), 50):  # API allows max 50 IDs per call
        batch = video_ids[i : i + 50]
        resp = (
            youtube.videos()
            .list(
                part="contentDetails,statistics",
                id=",".join(batch),
                maxResults=50,
            )
            .execute()
        )
        for item in resp["items"]:
            vid = item["id"]
            duration = item["contentDetails"]["duration"]
            view_count = item["statistics"].get("viewCount", "0")
            details[vid] = {
                "duration": duration,
                "viewCount": view_count,
            }
    return details


def get_all_videos(youtube, playlist_id: str) -> List[dict]:
    """Return a list of dicts with videoId, title, publishedAt, duration, and viewCount."""
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

    # Fetch duration and view count for all videos
    video_ids = [v["videoId"] for v in vids]
    details = get_video_details(youtube, video_ids)
    for v in vids:
        v.update(details.get(v["videoId"], {"duration": None, "viewCount": None}))
    return vids


def get_all_vids(channel_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)

    uploads_pid = get_uploads_playlist_id(youtube, channel_id)
    videos = get_all_videos(youtube, uploads_pid)

    print(f"{len(videos)} videos found on channel {channel_id}\n")
    return videos


def get_channel_vids_filtered(
    channel_id: str, sort_by: Literal["views", "upload_date"], min_vid_duration: int
):
    all_vids = get_all_vids(channel_id)
    if sort_by == "views":
        view_sorted = sorted(all_vids, key=lambda d: int(d["viewCount"]), reverse=True)
    else:
        view_sorted = sorted(
            all_vids,
            key=lambda d: datetime.strptime(d["publishedAt"], "%Y-%m-%dT%H:%M:%SZ"),
            reverse=True,
        )
    # video_print = "\n".join(
    #     f"{i + 1}. {v['title']} : {v['viewCount']}" for i, v in enumerate(view_sorted)
    # )
    # print(view_sorted[:10])
    vids_filtered = [
        vid
        for vid in view_sorted
        if int(isodate.parse_duration(vid["duration"]).total_seconds())
        > min_vid_duration
    ]
    print("duration filtered, ", len(vids_filtered))
    # print(vids_filtered[:50])
    return vids_filtered[:100]
