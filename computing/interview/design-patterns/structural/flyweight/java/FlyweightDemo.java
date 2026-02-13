package interview.designpatterns.structural.flyweight;

import java.util.HashMap;
import java.util.Map;

final class Glyph {
    private final char symbol;

    Glyph(char symbol) {
        this.symbol = symbol;
    }

    void render(int fontSize, int x, int y) {
        System.out.printf("Rendering '%c' size=%d at (%d, %d)%n", symbol, fontSize, x, y);
    }
}

final class GlyphFactory {
    private final Map<Character, Glyph> cache = new HashMap<>();

    Glyph get(char symbol) {
        return cache.computeIfAbsent(symbol, Glyph::new);
    }
}

public final class FlyweightDemo {
    private FlyweightDemo() {}

    public static void main(String[] args) {
        GlyphFactory factory = new GlyphFactory();
        String text = "FLY";
        int x = 0;
        for (char ch : text.toCharArray()) {
            factory.get(ch).render(12, x, 0);
            x += 10;
        }
    }
}
