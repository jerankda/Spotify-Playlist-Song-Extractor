# Spotify Playlist Song Extractor

This program allows you to extract a list of songs from a Spotify playlist by providing the playlist ID. 

## Getting Started

To run this program, you will need to have Python 3 installed on your system. You will also need to have the following libraries installed:
- requests
- json

You will also need a Spotify developer account and a Spotify API key to use the Spotify Web API.

### Prerequisites

1. Register for a Spotify developer account at [developer.spotify.com](https://developer.spotify.com/)
2. Create a new Spotify app and obtain an API key
3. Replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` in the code with your own API key.

### Running the program

1. Open the command prompt or terminal and navigate to the directory where the code is saved.
2. Run the command `python main.py`
3. The program will prompt you to enter the Spotify ID of the playlist. Enter the ID and press enter.
4. The program will display a loading animation while it's retrieving the songs from the Spotify Web API.
5. Once it has retrieved all the songs, it will then print the name of eachsong in the playlist

## Built With
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/) - Used to extract the songs from the playlist
- [Python](https://www.python.org/) - The programming language used to write the code


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

