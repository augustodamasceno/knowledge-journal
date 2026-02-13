package interview.designpatterns.structural.adapter;

interface Shape {
    void draw();
}

final class ModernCircle implements Shape {
    private final int radius;

    ModernCircle(int radius) {
        this.radius = radius;
    }

    @Override
    public void draw() {
        System.out.printf("Drawing modern circle r=%d%n", radius);
    }
}

final class LegacyRectangle {
    private final int x;
    private final int y;
    private final int width;
    private final int height;

    LegacyRectangle(int x, int y, int width, int height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    void oldDraw() {
        System.out.printf("Drawing legacy rectangle at (%d, %d) size %dx%d%n", x, y, width, height);
    }
}

final class RectangleAdapter implements Shape {
    private final LegacyRectangle adaptee;

    RectangleAdapter(int x, int y, int width, int height) {
        this.adaptee = new LegacyRectangle(x, y, width, height);
    }

    @Override
    public void draw() {
        adaptee.oldDraw();
    }
}

public final class AdapterDemo {
    private AdapterDemo() {}

    public static void main(String[] args) {
        Shape circle = new ModernCircle(5);
        Shape rectangle = new RectangleAdapter(10, 10, 20, 15);
        circle.draw();
        rectangle.draw();
    }
}
