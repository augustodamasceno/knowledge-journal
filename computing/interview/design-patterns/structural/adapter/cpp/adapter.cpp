#include <iostream>
#include <memory>

class Shape {
public:
    virtual ~Shape() = default;
    virtual void draw() const = 0;
};

class LegacyRectangle {
public:
    LegacyRectangle(int x, int y, int width, int height)
        : x_(x), y_(y), width_(width), height_(height) {}

    void old_draw() const {
        std::cout << "Drawing legacy rectangle at (" << x_ << ", " << y_
                  << ") size " << width_ << "x" << height_ << "\n";
    }

private:
    int x_;
    int y_;
    int width_;
    int height_;
};

class RectangleAdapter : public Shape {
public:
    RectangleAdapter(int x, int y, int width, int height)
        : adaptee_(x, y, width, height) {}

    void draw() const override { adaptee_.old_draw(); }

private:
    LegacyRectangle adaptee_;
};

class ModernCircle : public Shape {
public:
    explicit ModernCircle(int radius) : radius_(radius) {}

    void draw() const override {
        std::cout << "Drawing modern circle r=" << radius_ << "\n";
    }

private:
    int radius_;
};

void render_shape(const Shape& shape) {
    shape.draw();
}

int main() {
    ModernCircle circle(5);
    RectangleAdapter adapted_rect(10, 10, 20, 15);

    render_shape(circle);
    render_shape(adapted_rect);
}
