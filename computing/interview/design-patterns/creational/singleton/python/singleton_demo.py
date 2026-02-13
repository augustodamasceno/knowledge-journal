from __future__ import annotations
from threading import Lock


class Logger:
    _instance: Logger | None = None
    _lock = Lock()

    def __new__(cls) -> Logger:  # type: ignore[override]
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def log(self, message: str) -> None:
        print(f"[LOG] {message}")


def main() -> None:
    Logger().log("Starting process")
    Logger().log("Process completed")


if __name__ == "__main__":
    main()
