import requests
import json

# Replace with your own access token
access_token = "YOUR_ACCESS_TOKEN"

# Replace with the ID of the playlist
playlist_id = "PLAYLIST_ID"

# Make a GET request to the Spotify Web API
headers = {
    "Authorization": "Bearer {}".format(access_token)
}

playlist_endpoint = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
response = requests.get(playlist_endpoint, headers=headers)

# Get the JSON data from the response
data = json.loads(response.text)

# Extract the song names from the data
songs = [item["track"]["name"] for item in data["items"]]

# Print the list of songs
print(songs)
