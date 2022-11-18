import logging
from pathlib import Path
import subprocess  # noqa: S404
from typing import Any

from spotify_to_youtube.spotify.schemas.tracks import Track


class Metadata:
    def __init__(self, track: Track, playlist_name: str) -> None:
        self.track = track
        artist_names = ", ".join(artist.name for artist in track.artists)
        self._metadata: dict[str, Any] = {
            "artist": artist_names,
            # "artistsort": track.,
            "album": track.album.name,
            # "albumsort": track.,
            "albumartist": ", ".join(artist.name for artist in track.album.artists),
            # "albumartistsort": track.,
            "title": track.name,
            # "titlesort": track.,
            "track": track.track_number,
            "name": f"{artist_names} - {track.name}",
            # "genre": track.artists,
            "mood": playlist_name,
            "date": track.album.release_date,
            "originaldate": track.album.release_date,
            # "composer": track.,
            # "composersort": track.,
            "performer": artist_names,
            # "conductor": track.,
            "work": playlist_name,
            # "ensemble": track.,
            # "movement": track.,
            # "movementnumber": track.,
            # "location": track.,
            # "grouping": track.,
            # "comment": track.,
            "disc": track.disc_number,
            # "label": track.,
            # "musicbrainz_artistid": track.,
            # "musicbrainz_albumid": track.,
            # "musicbrainz_albumartistid": track.,
            # "musicbrainz_trackid": track.,
            # "musicbrainz_releasetrackid": track.,
            # "musicbrainz_workid": track.,
        }

    def add_to_file(self, mp3: Path) -> None:
        self._ffmpeg(mp3=mp3)

    def _ffmpeg(self, mp3: Path) -> None:
        opus = mp3.with_suffix(".opus")
        logging.info(opus)
        if opus.exists():
            return
        cmd: list[str] = ["ffmpeg", "-i", str(mp3), "-f", "mp3", "-y"]
        cmd.extend(self._add_metadata())
        cmd.extend(["-c", "copy", str(opus)])
        subprocess.run(cmd)  # noqa: S603
        mp3.unlink()

    def _add_metadata(self) -> list[str]:
        metadata: list[str] = []
        for tag_name, tag_val in self._metadata.items():
            metadata.extend(["-metadata", f"{tag_name}={tag_val}"])
        return metadata
