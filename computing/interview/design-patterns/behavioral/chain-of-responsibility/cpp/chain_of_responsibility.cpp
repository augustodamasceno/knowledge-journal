#include <iostream>
#include <memory>
#include <string>

enum class Severity { Info, Warning, Error };

struct LogRecord {
    Severity level;
    std::string message;
};

class Logger {
public:
    virtual ~Logger() = default;

    void set_next(std::shared_ptr<Logger> next) {
        next_ = std::move(next);
    }

    void handle(const LogRecord& record) const {
        if (should_handle(record.level)) {
            write(record.message);
        } else if (next_) {
            next_->handle(record);
        } else {
            std::cout << "No handler for message: " << record.message << "\n";
        }
    }

protected:
    virtual bool should_handle(Severity level) const = 0;
    virtual void write(const std::string& message) const = 0;

private:
    std::shared_ptr<Logger> next_;
};

class ConsoleLogger : public Logger {
protected:
    bool should_handle(Severity level) const override {
        return level == Severity::Info;
    }

    void write(const std::string& message) const override {
        std::cout << "Console: " << message << "\n";
    }
};

class FileLogger : public Logger {
protected:
    bool should_handle(Severity level) const override {
        return level == Severity::Warning;
    }

    void write(const std::string& message) const override {
        std::cout << "File: " << message << "\n";
    }
};

class AlertLogger : public Logger {
protected:
    bool should_handle(Severity level) const override {
        return level == Severity::Error;
    }

    void write(const std::string& message) const override {
        std::cout << "Alert: " << message << "\n";
    }
};

int main() {
    auto console = std::make_shared<ConsoleLogger>();
    auto file = std::make_shared<FileLogger>();
    auto alert = std::make_shared<AlertLogger>();

    console->set_next(file);
    file->set_next(alert);

    console->handle({Severity::Info, "Starting system"});
    console->handle({Severity::Warning, "Disk space low"});
    console->handle({Severity::Error, "Service offline"});
}
