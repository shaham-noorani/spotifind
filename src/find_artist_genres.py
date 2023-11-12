import json
import pandas as pd
import concurrent.futures

import requests
import base64
import webbrowser
import concurrent.futures
from urllib.parse import urlencode
import os
from dotenv import load_dotenv

load_dotenv()


# Function to fetch artist genres
def fetch_artist_genres(artist_id, token):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    data = response.json()
    genres = data.get("genres", [])

    return artist_id, genres[:3]


def find_artist_genres(token):
    liked_songs = pd.read_csv("data/liked_songs.tsv", sep="\t")
    artist_ids = liked_songs["Main Artist ID"].unique().tolist()

    # Create dictionary mapping artist id to top 3 genres
    artist_genres = {}

    # Use ThreadPoolExecutor to fetch artist genres concurrently
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_artist = {
            executor.submit(fetch_artist_genres, artist_id, token): artist_id
            for artist_id in artist_ids
        }
        for future in concurrent.futures.as_completed(future_to_artist):
            artist_id = future_to_artist[future]
            try:
                artist_id, genres = future.result()
                artist_genres[artist_id] = genres
            except Exception as exc:
                print(
                    f"An exception occurred while processing artist {artist_id}: {exc}"
                )

    # Write dictionary to JSON file
    with open("data/artist_genres.json", "w") as f:
        json.dump(artist_genres, f)
