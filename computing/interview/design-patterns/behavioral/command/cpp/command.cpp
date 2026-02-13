#include <iostream>
#include <memory>
#include <stack>
#include <string>

class Editor {
public:
    void append(const std::string& text) {
        content_ += text;
    }

    void remove_last(std::size_t length) {
        if (length <= content_.size()) {
            content_.erase(content_.size() - length);
        }
    }

    const std::string& content() const { return content_; }

private:
    std::string content_;
};

class Command {
public:
    virtual ~Command() = default;
    virtual void execute() = 0;
    virtual void undo() = 0;
};

class AppendCommand : public Command {
public:
    AppendCommand(Editor& editor, std::string text)
        : editor_(editor), text_(std::move(text)) {}

    void execute() override {
        editor_.append(text_);
    }

    void undo() override {
        editor_.remove_last(text_.size());
    }

private:
    Editor& editor_;
    std::string text_;
};

class Invoker {
public:
    void run_command(std::shared_ptr<Command> command) {
        command->execute();
        history_.push(std::move(command));
    }

    void undo_last() {
        if (history_.empty()) {
            std::cout << "Nothing to undo\n";
            return;
        }
        auto command = history_.top();
        history_.pop();
        command->undo();
    }

private:
    std::stack<std::shared_ptr<Command>> history_;
};

int main() {
    Editor editor;
    Invoker invoker;

    invoker.run_command(std::make_shared<AppendCommand>(editor, "Hello"));
    invoker.run_command(std::make_shared<AppendCommand>(editor, " World"));
    std::cout << "Content: " << editor.content() << "\n";

    invoker.undo_last();
    std::cout << "After undo: " << editor.content() << "\n";
}
