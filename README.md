# SpotiFind

## Overview

SpotiFind interacts with the Spotify API to fetch your liked songs and analyses them using OpenAI's GPT model for mood and genre classification. Based on your search query, it then recommends songs from your liked collection that match the specified criteria.

## Features

- Fetch and analyze user's liked songs from Spotify.
- Utilize OpenAI's GPT models to classify songs by mood and genre.
- Search functionality to find songs matching user-defined criteria.
- Save liked songs data to a local file for quick access.
- Interactive command-line interface for easy usage.

## Setup

### Prerequisites

- Python 3.6 or higher
- Spotify API credentials (Client ID and Client Secret)
- OpenAI API key

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/shaham-noorani/spotifind.git
   ```

2. Navigate to the project directory:

   ```bash
   cd spotifind
   ```

3. Install required dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Set up your .env file with Spotify and OpenAI credentials:

   ```bash
   touch .env
   ```

   ```bash
   SPOTIFY_CLIENT_ID='your_spotify_client_id'
   SPOTIFY_CLIENT_SECRET='your_spotify_client_secret'
   OPENAI_API_KEY='your_openai_api_key'
   ```

## Usage

Run the main script and follow the command-line prompts:

```bash
python main.py
```
