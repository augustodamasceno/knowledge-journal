#include <iostream>
#include <memory>
#include <vector>
#include <cmath>

class Shape {
public:
    virtual ~Shape() = default;
    virtual double area() const = 0;
    virtual void describe() const = 0;
};

class Circle : public Shape {
public:
    explicit Circle(double radius) : radius_(radius) {}

    double area() const override {
        return M_PI * radius_ * radius_;
    }

    void describe() const override {
        std::cout << "Circle radius=" << radius_ << " area=" << area() << "\n";
    }

private:
    double radius_;
};

class Rectangle : public Shape {
public:
    Rectangle(double width, double height) : width_(width), height_(height) {}

    double area() const override {
        return width_ * height_;
    }

    void describe() const override {
        std::cout << "Rectangle " << width_ << "x" << height_ << " area=" << area() << "\n";
    }

private:
    double width_;
    double height_;
};

int main() {
    std::vector<std::shared_ptr<Shape>> shapes;
    shapes.emplace_back(std::make_shared<Circle>(2.0));
    shapes.emplace_back(std::make_shared<Rectangle>(3.0, 4.0));

    for (const auto& shape : shapes) {
        shape->describe();
    }

    return 0;
}
