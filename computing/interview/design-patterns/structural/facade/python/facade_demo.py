from __future__ import annotations


class Amplifier:
    def on(self) -> None:
        print("Amplifier on")

    def set_volume(self, level: int) -> None:
        print(f"Amplifier volume {level}")


class StreamingPlayer:
    def on(self) -> None:
        print("Player on")

    def play_movie(self, title: str) -> None:
        print(f"Now playing: {title}")

    def stop(self) -> None:
        print("Stopping playback")


class Projector:
    def on(self) -> None:
        print("Projector on")

    def wide_screen_mode(self) -> None:
        print("Setting widescreen mode")


class HomeTheaterFacade:
    def __init__(self, amp: Amplifier, player: StreamingPlayer, projector: Projector) -> None:
        self._amp = amp
        self._player = player
        self._projector = projector

    def watch_movie(self, title: str) -> None:
        print("Get ready to watch a movie...")
        self._amp.on()
        self._amp.set_volume(7)
        self._projector.on()
        self._projector.wide_screen_mode()
        self._player.on()
        self._player.play_movie(title)

    def end_movie(self) -> None:
        print("Shutting movie theater down...")
        self._player.stop()


def main() -> None:
    theater = HomeTheaterFacade(Amplifier(), StreamingPlayer(), Projector())
    theater.watch_movie("Inception")
    theater.end_movie()


if __name__ == "__main__":
    main()
