import os.path
from make_reccomendations import search_songs
from save_liked_songs import save_liked_songs
from find_artist_genres import find_artist_genres

# check if liked_songs.tsv exists
if not os.path.isfile("data/liked_songs.tsv"):
    save_liked_songs()
    find_artist_genres()

else:
    query = input("Describe the music you're looking for: ")
    result = search_songs(query)
    print("Here are some songs I found:")
    for song in result:
        print(f"{song['Song Title']} by {song['Main Artist']}")
