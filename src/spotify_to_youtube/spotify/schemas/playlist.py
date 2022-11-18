from typing import Any, Optional

from pydantic import BaseModel


class ExternalUrls(BaseModel):
    spotify: str


class Followers(BaseModel):
    href: str
    total: int


class Image(BaseModel):
    url: str
    height: Optional[int]
    width: Optional[int]


class ExternalUrls1(BaseModel):
    spotify: str


class Followers1(BaseModel):
    href: str
    total: int


class Owner(BaseModel):
    external_urls: ExternalUrls1
    href: str
    id: str
    type: str
    uri: str
    display_name: str


class Tracks(BaseModel):
    href: str
    items: list[dict[str, Any]]
    limit: int
    next: str
    offset: int
    previous: str
    total: int


class PlaylistResponseModel(BaseModel):
    collaborative: bool
    description: str
    external_urls: ExternalUrls
    href: str
    id: str
    images: list[Image]
    name: str
    owner: Owner
    public: bool
    snapshot_id: str
    type: str
    uri: str
