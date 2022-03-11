# from app import env_variables
from dotenv import load_dotenv

load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret
)

sp = spotipy.Spotify(auth_manager=auth_manager)

# genres
# response = sp.recommendation_genre_seeds()["genres"]
# print(len(response), response)
query = "아이유"
# search
response = sp.search(query, limit=10, type="track")
# items = response["tracks"]["items"]

print(response)


def get_songs(query_type, query):
    if query_type == "artist":
        query = "artist:" + query
    else:
        query = "track:" + query
    response = sp.search(query, limit=20, type="track")
