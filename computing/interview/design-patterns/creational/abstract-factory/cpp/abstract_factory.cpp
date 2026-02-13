#include <iostream>
#include <memory>

struct Button {
    virtual ~Button() = default;
    virtual void render() const = 0;
};

struct Checkbox {
    virtual ~Checkbox() = default;
    virtual void toggle() const = 0;
};

struct GuiFactory {
    virtual ~GuiFactory() = default;
    virtual std::unique_ptr<Button> create_button() const = 0;
    virtual std::unique_ptr<Checkbox> create_checkbox() const = 0;
};

class WindowsButton : public Button {
public:
    void render() const override { std::cout << "Rendering Windows button\n"; }
};

class WindowsCheckbox : public Checkbox {
public:
    void toggle() const override { std::cout << "Toggling Windows checkbox\n"; }
};

class WindowsFactory : public GuiFactory {
public:
    std::unique_ptr<Button> create_button() const override { return std::make_unique<WindowsButton>(); }
    std::unique_ptr<Checkbox> create_checkbox() const override { return std::make_unique<WindowsCheckbox>(); }
};

class MacButton : public Button {
public:
    void render() const override { std::cout << "Rendering macOS button\n"; }
};

class MacCheckbox : public Checkbox {
public:
    void toggle() const override { std::cout << "Toggling macOS checkbox\n"; }
};

class MacFactory : public GuiFactory {
public:
    std::unique_ptr<Button> create_button() const override { return std::make_unique<MacButton>(); }
    std::unique_ptr<Checkbox> create_checkbox() const override { return std::make_unique<MacCheckbox>(); }
};

class Application {
public:
    explicit Application(std::unique_ptr<GuiFactory> factory) : factory_(std::move(factory)) {}

    void paint_ui() const {
        auto button = factory_->create_button();
        auto checkbox = factory_->create_checkbox();
        button->render();
        checkbox->toggle();
    }

private:
    std::unique_ptr<GuiFactory> factory_;
};

int main() {
    Application windows_app(std::make_unique<WindowsFactory>());
    windows_app.paint_ui();

    Application mac_app(std::make_unique<MacFactory>());
    mac_app.paint_ui();
}
