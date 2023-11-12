import os.path

from src.save_liked_songs import save_liked_songs
from src.find_artist_genres import find_artist_genres
from src.make_recommendations import search_songs

# check if liked_songs.tsv exists
if not os.path.isfile("data/liked_songs.tsv"):
    token = save_liked_songs()
    find_artist_genres(token)

else:
    query = input("Describe the music you're looking for: ")
    result = search_songs(query)
    print("Here are some songs I found:")
    for song in result:
        print(f"{song['Song Title']} by {song['Main Artist']}")
