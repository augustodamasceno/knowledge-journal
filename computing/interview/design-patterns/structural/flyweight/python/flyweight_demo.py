from __future__ import annotations


class Glyph:
    def __init__(self, symbol: str) -> None:
        self._symbol = symbol

    def render(self, font_size: int, x: int, y: int) -> None:
        print(f"Rendering '{self._symbol}' size={font_size} at ({x}, {y})")


class GlyphFactory:
    def __init__(self) -> None:
        self._cache: dict[str, Glyph] = {}

    def get(self, symbol: str) -> Glyph:
        try:
            return self._cache[symbol]
        except KeyError:
            glyph = Glyph(symbol)
            self._cache[symbol] = glyph
            return glyph


def main() -> None:
    factory = GlyphFactory()
    text = "FLY"
    x = 0
    for ch in text:
        factory.get(ch).render(12, x, 0)
        x += 10


if __name__ == "__main__":
    main()
