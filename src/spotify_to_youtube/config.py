from pathlib import Path

from pydantic import BaseSettings

from spotify_to_youtube.version import __version__


class BaseConfig(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class SpotifyConfig(BaseConfig):
    client_id: str
    client_secret: str

    class Config:
        env_prefix = "spotify_"


class LogConfig(BaseConfig):
    level: str = "INFO"

    class Config:
        env_prefix = "log_"


class AppConfig(BaseConfig):
    output_dir: Path = Path.home().joinpath("music")


class Config:
    def __init__(self) -> None:
        self.version: str = __version__
        self.spotify = SpotifyConfig()
        self.app = AppConfig()
        self.log = LogConfig()
