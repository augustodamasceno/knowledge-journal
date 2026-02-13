#include <iostream>
#include <mutex>

class Logger {
public:
    static Logger& instance() {
        static Logger instance;
        return instance;
    }

    void log(const std::string& message) {
        std::lock_guard<std::mutex> lock(mutex_);
        std::cout << "[LOG] " << message << '\n';
    }

private:
    Logger() = default;
    std::mutex mutex_;
};

int main() {
    Logger::instance().log("Starting process");
    Logger::instance().log("Process completed");
}
