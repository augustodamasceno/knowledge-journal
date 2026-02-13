#include <iostream>
#include <memory>
#include <string>
#include <unordered_map>

class Glyph {
public:
    explicit Glyph(char symbol) : symbol_(symbol) {}

    void render(int font_size, int x, int y) const {
        std::cout << "Rendering '" << symbol_ << "' size=" << font_size
                  << " at (" << x << ", " << y << ")\n";
    }

private:
    char symbol_;
};

class GlyphFactory {
public:
    std::shared_ptr<Glyph> get(char symbol) {
        auto it = cache_.find(symbol);
        if (it != cache_.end()) {
            return it->second;
        }

        auto glyph = std::make_shared<Glyph>(symbol);
        cache_[symbol] = glyph;
        return glyph;
    }

private:
    std::unordered_map<char, std::shared_ptr<Glyph>> cache_;
};

int main() {
    GlyphFactory factory;
    std::string text = "FLY";

    int x = 0;
    for (char ch : text) {
        auto glyph = factory.get(ch);
        glyph->render(12, x, 0);
        x += 10;
    }
}
