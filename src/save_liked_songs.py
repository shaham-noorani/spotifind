import requests
import base64
import webbrowser
import concurrent.futures
from urllib.parse import urlencode
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Spotify Client Credentials
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

# Step 1: Obtain Authorization Code
auth_headers = {
    "client_id": client_id,
    "response_type": "code",
    "redirect_uri": "http://localhost:5000/callback/",
    "scope": "user-library-read",
}


def save_liked_songs():
    webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))
    code = input("Enter the authorization code from the URL: ")

    # Step 2: Obtain Authorization Token
    encoded_credentials = base64.b64encode(
        client_id.encode() + b":" + client_secret.encode()
    ).decode("utf-8")

    token_headers = {
        "Authorization": "Basic " + encoded_credentials,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://localhost:5000/callback/",
    }

    print("Requesting token...")

    r = requests.post(
        "https://accounts.spotify.com/api/token", data=token_data, headers=token_headers
    )
    token = r.json()["access_token"]

    # Step 3: Use the Authorization Token to Query Your Saved Tracks
    user_headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
    }

    # Function to fetch a batch of songs
    def fetch_songs(i):
        print(f"Fetching songs {i}-{i+50}...")
        user_params = {"limit": 50, "offset": i}
        user_tracks_response = requests.get(
            "https://api.spotify.com/v1/me/tracks",
            params=user_params,
            headers=user_headers,
        )

        liked_songs = user_tracks_response.json()["items"]
        song_data = []
        for song in liked_songs:
            track = song["track"]
            main_artist_name = track["artists"][0]["name"]
            main_artist_id = track["artists"][0]["id"]
            song_title = track["name"]
            album_name = track["album"]["name"]
            release_date = track["album"]["release_date"]
            song_data.append(
                f"{song_title}\t{main_artist_name}\t{main_artist_id}\t{album_name}\t{release_date}\n"
            )
        return song_data

    # Step 4: Get all liked songs (50 at a time) and save to csv
    with open("data/liked_songs.tsv", "w") as f:
        f.write("Song Title\tMain Artist\tMain Artist ID\tAlbum Name\tRelease Date\n")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(fetch_songs, range(0, 5000, 50))
            for result in results:
                f.writelines(result)

    return token


save_liked_songs()
