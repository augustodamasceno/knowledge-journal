from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import List


class Playlist(Iterable[str]):
    def __init__(self) -> None:
        self._tracks: List[str] = []

    def add_track(self, name: str) -> None:
        self._tracks.append(name)

    def __iter__(self) -> Iterator[str]:
        return _PlaylistIterator(self._tracks)


class _PlaylistIterator(Iterator[str]):
    def __init__(self, tracks: List[str]) -> None:
        self._tracks = tracks
        self._index = 0

    def __next__(self) -> str:
        if self._index >= len(self._tracks):
            raise StopIteration
        value = self._tracks[self._index]
        self._index += 1
        return value


def main() -> None:
    playlist = Playlist()
    playlist.add_track("Intro")
    playlist.add_track("Theme")
    playlist.add_track("Outro")

    for track in playlist:
        print(f"Track: {track}")


if __name__ == "__main__":
    main()
