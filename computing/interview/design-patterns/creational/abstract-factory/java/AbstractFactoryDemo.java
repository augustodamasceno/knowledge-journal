package interview.designpatterns.creational.abstractfactory;

interface Button {
    void render();
}

interface Checkbox {
    void toggle();
}

interface GuiFactory {
    Button createButton();
    Checkbox createCheckbox();
}

final class WindowsButton implements Button {
    @Override
    public void render() {
        System.out.println("Rendering Windows button");
    }
}

final class WindowsCheckbox implements Checkbox {
    @Override
    public void toggle() {
        System.out.println("Toggling Windows checkbox");
    }
}

final class WindowsFactory implements GuiFactory {
    @Override
    public Button createButton() {
        return new WindowsButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }
}

final class MacButton implements Button {
    @Override
    public void render() {
        System.out.println("Rendering macOS button");
    }
}

final class MacCheckbox implements Checkbox {
    @Override
    public void toggle() {
        System.out.println("Toggling macOS checkbox");
    }
}

final class MacFactory implements GuiFactory {
    @Override
    public Button createButton() {
        return new MacButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new MacCheckbox();
    }
}

public final class AbstractFactoryDemo {
    private AbstractFactoryDemo() {}

    public static void main(String[] args) {
        Application windowsApp = new Application(new WindowsFactory());
        windowsApp.paintUi();

        Application macApp = new Application(new MacFactory());
        macApp.paintUi();
    }
}

final class Application {
    private final GuiFactory factory;

    Application(GuiFactory factory) {
        this.factory = factory;
    }

    void paintUi() {
        Button button = factory.createButton();
        Checkbox checkbox = factory.createCheckbox();
        button.render();
        checkbox.toggle();
    }
}
