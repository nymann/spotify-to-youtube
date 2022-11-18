import requests
from spotipy.oauth2 import SpotifyClientCredentials

from spotify_to_youtube.spotify.schemas.playlist import PlaylistResponseModel
from spotify_to_youtube.spotify.schemas.tracks import TracksResponseModel


class SpotifyClient:
    def __init__(self, client_id: str, client_secret: str, playlist_id: str) -> None:
        self.playlist_id = self.normalize_playlist_id(playlist_id=playlist_id)
        creds = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.access_token = creds.get_access_token(as_dict=False)
        self.headers = {"Authorization": f"Bearer {self.access_token}"}
        self.base_url = "https://api.spotify.com/v1"

    @staticmethod
    def normalize_playlist_id(playlist_id: str) -> str:
        if "playlist/" in playlist_id:
            p_id = playlist_id
            playlist_id = p_id[p_id.index("playlist/") + len("playlist/") :]
        if "?" in playlist_id:
            playlist_id = playlist_id[: playlist_id.index("?")]
        return playlist_id

    def playlist(self) -> PlaylistResponseModel:
        url = f"{self.base_url}/playlists/{self.playlist_id}"
        return PlaylistResponseModel(
            **requests.get(url=url, headers=self.headers).json(),
        )

    def tracks(self) -> TracksResponseModel:
        url = f"{self.base_url}/playlists/{self.playlist_id}/tracks"
        return TracksResponseModel(
            **requests.get(
                url=url,
                headers=self.headers,
            ).json(),
        )
