package interview.designpatterns.structural.bridge;

interface Renderer {
    void renderCircle(double radius);
}

final class VectorRenderer implements Renderer {
    @Override
    public void renderCircle(double radius) {
        System.out.printf("Vector circle radius=%.2f%n", radius);
    }
}

final class RasterRenderer implements Renderer {
    @Override
    public void renderCircle(double radius) {
        System.out.printf("Raster circle radius=%.2f%n", radius);
    }
}

abstract class Shape {
    private final Renderer renderer;

    protected Shape(Renderer renderer) {
        this.renderer = renderer;
    }

    protected Renderer renderer() {
        return renderer;
    }

    abstract void draw();
}

final class Circle extends Shape {
    private final double radius;

    Circle(Renderer renderer, double radius) {
        super(renderer);
        this.radius = radius;
    }

    @Override
    void draw() {
        renderer().renderCircle(radius);
    }
}

public final class BridgeDemo {
    private BridgeDemo() {}

    public static void main(String[] args) {
        Shape vectorCircle = new Circle(new VectorRenderer(), 2.5);
        Shape rasterCircle = new Circle(new RasterRenderer(), 2.5);
        vectorCircle.draw();
        rasterCircle.draw();
    }
}
