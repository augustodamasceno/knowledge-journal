from __future__ import annotations


class Image:
    def display(self) -> None:
        raise NotImplementedError


class RealImage(Image):
    def __init__(self, filename: str) -> None:
        self._filename = filename
        print(f"Loading image from disk: {filename}")

    def display(self) -> None:
        print(f"Displaying image: {self._filename}")


class LazyImageProxy(Image):
    def __init__(self, filename: str) -> None:
        self._filename = filename
        self._real_image: RealImage | None = None

    def display(self) -> None:
        if self._real_image is None:
            self._real_image = RealImage(self._filename)
        self._real_image.display()


def main() -> None:
    proxy: Image = LazyImageProxy("photo.png")
    print("First display triggers load:")
    proxy.display()
    print("Second display reuses loaded image:")
    proxy.display()


if __name__ == "__main__":
    main()
