#include <cstring>
#include <iostream>
#include <utility>

class Buffer {
public:
    Buffer() = default;

    explicit Buffer(const char* source) {
        std::size_t len = std::strlen(source);
        data_ = new char[len + 1];
        std::memcpy(data_, source, len + 1);
    }

    // Copy constructor
    Buffer(const Buffer& other) {
        if (other.data_) {
            std::size_t len = std::strlen(other.data_);
            data_ = new char[len + 1];
            std::memcpy(data_, other.data_, len + 1);
        }
    }

    // Copy assignment
    Buffer& operator=(const Buffer& other) {
        if (this == &other) {
            return *this;
        }
        Buffer temp(other);
        swap(temp);
        return *this;
    }

    // Move constructor
    Buffer(Buffer&& other) noexcept : data_(std::exchange(other.data_, nullptr)) {}

    // Move assignment
    Buffer& operator=(Buffer&& other) noexcept {
        if (this == &other) {
            return *this;
        }
        delete[] data_;
        data_ = std::exchange(other.data_, nullptr);
        return *this;
    }

    ~Buffer() {
        delete[] data_;
    }

    const char* c_str() const {
        return data_ ? data_ : "";
    }

private:
    void swap(Buffer& other) noexcept {
        std::swap(data_, other.data_);
    }

    char* data_ = nullptr;
};

int main() {
    Buffer greeting("hello");
    Buffer copy = greeting;             // copy constructor
    Buffer moved = std::move(greeting); // move constructor

    Buffer assigned;
    assigned = copy;                    // copy assignment
    assigned = Buffer("world");        // move assignment

    std::cout << "copy: " << copy.c_str() << '\n';
    std::cout << "assigned: " << assigned.c_str() << '\n';
    std::cout << "moved: " << moved.c_str() << '\n';
}
