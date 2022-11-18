import logging
from pathlib import Path
import subprocess  # noqa: S404

from spotify_to_youtube.metadata import Metadata
from spotify_to_youtube.spotify.schemas.playlist import PlaylistResponseModel
from spotify_to_youtube.spotify.schemas.tracks import Track
from spotify_to_youtube.spotify.schemas.tracks import TracksResponseModel


class YoutubeTrackDownloader:
    def __init__(self, playlist_name: str) -> None:
        self.playlist_name = playlist_name
        self.out_dir = Path(self.playlist_name)
        self.out_dir.mkdir(exist_ok=True)

    def download(self, track: Track) -> Path:  # noqa: WPS210
        artist = ", ".join(artist.name for artist in track.artists)
        title = track.name
        search_query = f"{artist} - {title}"
        output_file = self.out_dir.joinpath(f"{search_query}.mp3")
        if output_file.with_suffix(".opus").exists():
            return output_file
        filename = f"{search_query}.%(ext)s"
        logging.info("Downloading: %s", filename)
        output = str(self.out_dir.joinpath(filename))
        logging.warning(output)
        subprocess.run(  # noqa: S607, S603
            [
                "yt-dlp",
                "--output",
                output,
                "--extract-audio",
                "--audio-format",
                "mp3",
                "--audio-quality",
                "0",
                "--playlist-items",
                "1",
                "--quiet",
                "--default-search",
                "https://music.youtube.com/search?q=",
                search_query,
            ],
            check=True,
        )
        return output_file


class YoutubePlaylistDownloader:
    def download(self, track_response: TracksResponseModel, playlist: PlaylistResponseModel) -> None:
        track_downloader = YoutubeTrackDownloader(playlist_name=playlist.name)
        for track_item in track_response.items:
            try:
                mp3 = track_downloader.download(track=track_item.track)
            except subprocess.CalledProcessError as error:
                logging.error(error)
                continue
            metadata = Metadata(track=track_item.track, playlist_name=track_downloader.playlist_name)
            metadata.add_to_file(mp3=mp3)
