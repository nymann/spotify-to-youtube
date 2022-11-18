import logging
import sys

import typer

from spotify_to_youtube.config import Config
from spotify_to_youtube.downloader.youtube import YoutubePlaylistDownloader
from spotify_to_youtube.spotify.client import SpotifyClient

app = typer.Typer()


@app.command()
def main(playlist_id: str) -> None:
    config = Config()
    logging.basicConfig(stream=sys.stdout, level=config.log.level)
    spotify = SpotifyClient(
        client_id=config.spotify.client_id,
        client_secret=config.spotify.client_secret,
        playlist_id=playlist_id,
    )
    playlist_downloader = YoutubePlaylistDownloader()
    playlist_downloader.download(
        track_response=spotify.tracks(),
        playlist=spotify.playlist(),
    )


if __name__ == "__main__":
    app()
