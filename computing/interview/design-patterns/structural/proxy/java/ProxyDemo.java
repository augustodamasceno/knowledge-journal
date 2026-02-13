package interview.designpatterns.structural.proxy;

interface Image {
    void display();
}

final class RealImage implements Image {
    private final String filename;

    RealImage(String filename) {
        this.filename = filename;
        System.out.printf("Loading image from disk: %s%n", filename);
    }

    @Override
    public void display() {
        System.out.printf("Displaying image: %s%n", filename);
    }
}

final class LazyImageProxy implements Image {
    private final String filename;
    private RealImage realImage;

    LazyImageProxy(String filename) {
        this.filename = filename;
    }

    @Override
    public void display() {
        if (realImage == null) {
            realImage = new RealImage(filename);
        }
        realImage.display();
    }
}

public final class ProxyDemo {
    private ProxyDemo() {}

    public static void main(String[] args) {
        Image proxy = new LazyImageProxy("photo.png");
        System.out.println("First display triggers load:");
        proxy.display();
        System.out.println("Second display reuses loaded image:");
        proxy.display();
    }
}
