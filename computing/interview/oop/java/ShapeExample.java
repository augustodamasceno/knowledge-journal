package interview.oop;

import java.util.ArrayList;
import java.util.List;

abstract class Shape {
    abstract double area();
    abstract void describe();
}

final class Circle extends Shape {
    private final double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    @Override
    double area() {
        return Math.PI * radius * radius;
    }

    @Override
    void describe() {
        System.out.printf("Circle radius=%.2f area=%.3f%n", radius, area());
    }
}

final class Rectangle extends Shape {
    private final double width;
    private final double height;

    Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    @Override
    double area() {
        return width * height;
    }

    @Override
    void describe() {
        System.out.printf("Rectangle %.2fx%.2f area=%.3f%n", width, height, area());
    }
}

public final class ShapeExample {
    private ShapeExample() {}

    public static void main(String[] args) {
        List<Shape> shapes = new ArrayList<>();
        shapes.add(new Circle(2.0));
        shapes.add(new Rectangle(3.0, 4.0));

        for (Shape shape : shapes) {
            shape.describe();
        }
    }
}
