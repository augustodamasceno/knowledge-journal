#include <iostream>
#include <stack>
#include <string>

class TextMemento {
public:
    explicit TextMemento(std::string state) : state_(std::move(state)) {}
    const std::string& state() const { return state_; }

private:
    std::string state_;
};

class TextEditor {
public:
    void type(const std::string& text) {
        content_ += text;
    }

    TextMemento save() const {
        return TextMemento(content_);
    }

    void restore(const TextMemento& memento) {
        content_ = memento.state();
    }

    const std::string& content() const { return content_; }

private:
    std::string content_;
};

class History {
public:
    void push(const TextMemento& memento) {
        snapshots_.push(memento);
    }

    TextMemento pop() {
        if (snapshots_.empty()) {
            throw std::runtime_error("No states saved");
        }
        TextMemento memento = snapshots_.top();
        snapshots_.pop();
        return memento;
    }

private:
    std::stack<TextMemento> snapshots_;
};

int main() {
    TextEditor editor;
    History history;

    editor.type("Hello");
    history.push(editor.save());

    editor.type(" World");
    std::cout << "Current: " << editor.content() << '\n';

    editor.restore(history.pop());
    std::cout << "After undo: " << editor.content() << '\n';
}
