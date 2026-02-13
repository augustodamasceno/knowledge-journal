#include <iostream>
#include <memory>
#include <string>
#include <vector>

class FileSystemEntry {
public:
    explicit FileSystemEntry(std::string name) : name_(std::move(name)) {}
    virtual ~FileSystemEntry() = default;

    virtual void print(int indent) const = 0;

protected:
    void indent(int level) const {
        for (int i = 0; i < level; ++i) {
            std::cout << "  ";
        }
    }

    std::string name_;
};

class File : public FileSystemEntry {
public:
    explicit File(std::string name) : FileSystemEntry(std::move(name)) {}

    void print(int indent_level) const override {
        indent(indent_level);
        std::cout << "File: " << name_ << '\n';
    }
};

class Directory : public FileSystemEntry {
public:
    explicit Directory(std::string name) : FileSystemEntry(std::move(name)) {}

    void add(std::shared_ptr<FileSystemEntry> entry) {
        children_.push_back(std::move(entry));
    }

    void print(int indent_level) const override {
        indent(indent_level);
        std::cout << "Dir: " << name_ << '\n';
        for (const auto& child : children_) {
            child->print(indent_level + 1);
        }
    }

private:
    std::vector<std::shared_ptr<FileSystemEntry>> children_;
};

int main() {
    auto root = std::make_shared<Directory>("root");
    auto docs = std::make_shared<Directory>("docs");
    auto img = std::make_shared<File>("image.png");

    docs->add(std::make_shared<File>("resume.pdf"));
    root->add(docs);
    root->add(img);

    root->print(0);
}
