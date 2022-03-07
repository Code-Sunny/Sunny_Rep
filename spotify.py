from spotify_auth import sp

# Searth
# search_str = "윤하"
# result = sp.search(search_str)
# items = result["tracks"]["items"]

# for item in items:
#     album = item["album"]
#     artist = album["artists"][0]["name"]
#     image = album["images"][0]["url"]
#     album_title = album["name"]
#     print(artist, album_title)
#     print(image, "\n")

# # Show album
urn = "spotify:artist:6GwM5CHqhWXzG3l5kzRSAS"
response = sp.artist_albums(urn)

items = response["items"]

for item in items:
    print(item["name"])
