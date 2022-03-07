from app import env_variables
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = env_variables["spotify_id"]
client_secret = env_variables["spotify_secret"]

auth_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret
)

sp = spotipy.Spotify(auth_manager=auth_manager)
