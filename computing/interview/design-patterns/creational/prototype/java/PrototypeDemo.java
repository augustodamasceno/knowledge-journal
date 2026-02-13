package interview.designpatterns.creational.prototype;

import java.util.HashMap;
import java.util.Map;

abstract class DiagramNode {
    private final String label;

    DiagramNode(String label) {
        this.label = label;
    }

    String label() {
        return label;
    }

    abstract DiagramNode cloneNode();
    abstract void render();
}

final class CircleNode extends DiagramNode {
    private final double radius;

    CircleNode(String label, double radius) {
        super(label);
        this.radius = radius;
    }

    @Override
    DiagramNode cloneNode() {
        return new CircleNode(label(), radius);
    }

    @Override
    void render() {
        System.out.printf("Circle(%s, r=%.1f)%n", label(), radius);
    }
}

final class RectangleNode extends DiagramNode {
    private final double width;
    private final double height;

    RectangleNode(String label, double width, double height) {
        super(label);
        this.width = width;
        this.height = height;
    }

    @Override
    DiagramNode cloneNode() {
        return new RectangleNode(label(), width, height);
    }

    @Override
    void render() {
        System.out.printf("Rectangle(%s, %.1fx%.1f)%n", label(), width, height);
    }
}

final class PrototypeRegistry {
    private final Map<String, DiagramNode> prototypes = new HashMap<>();

    void registerNode(String name, DiagramNode node) {
        prototypes.put(name, node);
    }

    DiagramNode create(String name) {
        DiagramNode prototype = prototypes.get(name);
        if (prototype == null) {
            throw new IllegalArgumentException("Prototype not found");
        }
        return prototype.cloneNode();
    }
}

public final class PrototypeDemo {
    private PrototypeDemo() {}

    public static void main(String[] args) {
        PrototypeRegistry registry = new PrototypeRegistry();
        registry.registerNode("small_circle", new CircleNode("Small", 1.0));
        registry.registerNode("wide_rect", new RectangleNode("Wide", 3.0, 1.0));

        registry.create("small_circle").render();
        registry.create("wide_rect").render();
    }
}
