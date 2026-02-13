#include <iostream>
#include <memory>
#include <string>

struct Connection {
    explicit Connection(std::string endpoint) : endpoint(std::move(endpoint)) {
        std::cout << "opening " << this->endpoint << '\n';
    }

    ~Connection() {
        std::cout << "closing " << endpoint << '\n';
    }

    void send(const std::string& payload) {
        std::cout << "sending '" << payload << "' via " << endpoint << '\n';
    }

    std::string endpoint;
};

std::unique_ptr<Connection> make_unique_connection() {
    // unique_ptr enforces single owner and default delete suffices.
    return std::make_unique<Connection>("tcp://localhost:4000");
}

std::shared_ptr<Connection> make_shared_connection() {
    auto customCloser = [](Connection* conn) {
        std::cout << "custom cleanup before destruction\n";
        delete conn;
    };
    // shared_ptr allows multiple owners and custom deleter.
    return std::shared_ptr<Connection>(new Connection("udp://localhost:5000"), customCloser);
}

int main() {
    auto uniqueConn = make_unique_connection();
    uniqueConn->send("ping");

    auto sharedA = make_shared_connection();
    {
        auto sharedB = sharedA; // increments reference count
        sharedB->send("hello");
        std::cout << "use_count inside scope: " << sharedA.use_count() << '\n';
    }

    std::cout << "use_count after scope: " << sharedA.use_count() << '\n';
}
