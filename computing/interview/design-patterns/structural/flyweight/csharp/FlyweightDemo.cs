using System;
using System.Collections.Generic;

namespace Interview.DesignPatterns.Structural.Flyweight
{
    public sealed class Glyph
    {
        private readonly char _symbol;

        public Glyph(char symbol)
        {
            _symbol = symbol;
        }

        public void Render(int fontSize, int x, int y)
        {
            Console.WriteLine($"Rendering '{_symbol}' size={fontSize} at ({x}, {y})");
        }
    }

    public sealed class GlyphFactory
    {
        private readonly Dictionary<char, Glyph> _cache = new();

        public Glyph Get(char symbol)
        {
            if (_cache.TryGetValue(symbol, out var glyph))
            {
                return glyph;
            }

            glyph = new Glyph(symbol);
            _cache[symbol] = glyph;
            return glyph;
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var factory = new GlyphFactory();
            const string text = "FLY";
            var x = 0;
            foreach (var ch in text)
            {
                factory.Get(ch).Render(12, x, 0);
                x += 10;
            }
        }
    }
}
