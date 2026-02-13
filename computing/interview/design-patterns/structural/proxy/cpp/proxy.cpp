#include <iostream>
#include <memory>
#include <optional>
#include <string>

class Image {
public:
    virtual ~Image() = default;
    virtual void display() const = 0;
};

class RealImage : public Image {
public:
    explicit RealImage(std::string filename) : filename_(std::move(filename)) {
        std::cout << "Loading image from disk: " << filename_ << "\n";
    }

    void display() const override {
        std::cout << "Displaying image: " << filename_ << "\n";
    }

private:
    std::string filename_;
};

class LazyImageProxy : public Image {
public:
    explicit LazyImageProxy(std::string filename) : filename_(std::move(filename)) {}

    void display() const override {
        if (!real_image_) {
            real_image_ = std::make_shared<RealImage>(filename_);
        }
        real_image_->display();
    }

private:
    std::string filename_;
    mutable std::shared_ptr<RealImage> real_image_;
};

int main() {
    LazyImageProxy proxy("photo.png");
    std::cout << "First display triggers load:\n";
    proxy.display();
    std::cout << "Second display reuses loaded image:\n";
    proxy.display();
}
