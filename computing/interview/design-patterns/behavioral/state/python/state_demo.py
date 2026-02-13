from __future__ import annotations
from abc import ABC, abstractmethod


class PlayerState(ABC):
    @abstractmethod
    def play(self, player: AudioPlayer) -> None:
        ...

    @abstractmethod
    def pause(self, player: AudioPlayer) -> None:
        ...


class AudioPlayer:
    def __init__(self) -> None:
        self._state: PlayerState = PausedState()
        self.track = ""

    def set_state(self, state: PlayerState) -> None:
        self._state = state

    def set_track(self, track: str) -> None:
        self.track = track
        print(f"Current track: {self.track}")

    def play(self) -> None:
        self._state.play(self)

    def pause(self) -> None:
        self._state.pause(self)


class PlayingState(PlayerState):
    def play(self, player: AudioPlayer) -> None:
        print(f"Already playing {player.track}")

    def pause(self, player: AudioPlayer) -> None:
        print("Pausing playback")
        player.set_state(PausedState())


class PausedState(PlayerState):
    def play(self, player: AudioPlayer) -> None:
        print(f"Resuming playback of {player.track}")
        player.set_state(PlayingState())

    def pause(self, player: AudioPlayer) -> None:
        print("Already paused")


def main() -> None:
    player = AudioPlayer()
    player.set_track("Track 1")
    player.play()
    player.pause()
    player.play()


if __name__ == "__main__":
    main()
