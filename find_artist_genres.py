import json
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# Load artist ids from liked_songs.csv
def find_artist_genres():
    liked_songs = pd.read_csv("data/liked_songs.tsv", sep="\t")
    artist_ids = liked_songs["Main Artist ID"].unique().tolist()

    # Authenticate with Spotify API
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Create dictionary mapping artist id to top 3 genres
    artist_genres = {}
    for artist_id in artist_ids:
        genres = sp.artist(artist_id)["genres"][:3]
        artist_genres[artist_id] = genres

    # Write dictionary to JSON file
    with open("data/artist_genres.json", "w") as f:
        json.dump(artist_genres, f)
