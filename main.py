import requests
import json

client_id = "7050f6a9e8f644449a4751f35dc598ba"
client_secret = "959e5f9b5872469c8652b3d51dadff80"

# Get access token
response = requests.post(
    "https://accounts.spotify.com/api/token",
    data={
        "grant_type": "client_credentials",
    },
    auth=(client_id, client_secret),
)
response.raise_for_status()
data = json.loads(response.text)
access_token = data["access_token"]
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

playlist_id = input("Enter the Spotify ID of the playlist: ")

limit = 100 # Number of tracks to retrieve per request
offset = 0 # Initial offset

while True:
    response = requests.get(
        f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit={limit}&offset={offset}",
        headers=headers
    )
    response.raise_for_status()
    data = json.loads(response.text)
    songs = data["tracks"]["items"]
    total = data["tracks"]["total"]
    if not songs:
        break
    for song in songs:
        print(song["track"]["name"])
    offset += limit
    if offset >= total:
        break
