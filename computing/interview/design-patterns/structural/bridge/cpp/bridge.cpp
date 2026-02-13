#include <iostream>
#include <memory>

class Renderer {
public:
    virtual ~Renderer() = default;
    virtual void render_circle(double radius) const = 0;
};

class VectorRenderer : public Renderer {
public:
    void render_circle(double radius) const override {
        std::cout << "Vector circle radius=" << radius << "\n";
    }
};

class RasterRenderer : public Renderer {
public:
    void render_circle(double radius) const override {
        std::cout << "Raster circle radius=" << radius << "\n";
    }
};

class Shape {
public:
    explicit Shape(std::shared_ptr<Renderer> renderer) : renderer_(std::move(renderer)) {}
    virtual ~Shape() = default;
    virtual void draw() const = 0;

protected:
    std::shared_ptr<Renderer> renderer_;
};

class Circle : public Shape {
public:
    Circle(std::shared_ptr<Renderer> renderer, double radius)
        : Shape(std::move(renderer)), radius_(radius) {}

    void draw() const override {
        renderer_->render_circle(radius_);
    }

private:
    double radius_;
};

int main() {
    auto vector_renderer = std::make_shared<VectorRenderer>();
    auto raster_renderer = std::make_shared<RasterRenderer>();

    Circle vector_circle(vector_renderer, 2.5);
    Circle raster_circle(raster_renderer, 2.5);

    vector_circle.draw();
    raster_circle.draw();
}
