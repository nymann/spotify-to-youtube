# Spotify To YouTube

Downloads a Spotify playlist via YouTube Music.

## External dependencies

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [ffmpeg](https://github.com/FFmpeg/FFmpeg)

## Getting Started

1. Acquire a Spotify client id and client secret, read more [here](https://developer.spotify.com/documentation/web-api/quick-start/)
2. Set/export variables seen in `example.env`.
3. `spotify_to_youtube url-to-playlist`

### Examples

```sh
spotify_to_youtube https://open.spotify.com/playlist/0umdrbA6i3NOIH5N9wNX1J\?si\=d87e17e6bbb54613
```

Is equivalent to:

```sh
spotify_to_youtube 0umdrbA6i3NOIH5N9wNX1J
```

## Development

For help getting started developing check [DEVELOPMENT.md](DEVELOPMENT.md)
