from dotenv import load_dotenv
import os
import requests

load_dotenv()
YT_KEY = os.getenv("YOUTUBE_KEY")

URL = "https://www.googleapis.com/youtube/v3/search"


def get_youtube(query):
    params = {
        "key": YT_KEY,
        "part": "snippet",
        "type": "video",
        "q": query,
        "maxResults": 1,
        "order": "viewCount",
    }
    res = requests.get(URL, params=params).json()
    video_id = res["items"][0]["id"]["videoId"]
    video_link = f"https://youtube.com/watch?v={video_id}"
    return video_link


print(get_youtube("그래서 그래"))
