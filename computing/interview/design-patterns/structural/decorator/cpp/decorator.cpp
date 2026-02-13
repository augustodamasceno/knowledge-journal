#include <iostream>
#include <memory>
#include <string>

class DataSource {
public:
    virtual ~DataSource() = default;
    virtual std::string read() const = 0;
};

class FileDataSource : public DataSource {
public:
    explicit FileDataSource(std::string contents) : contents_(std::move(contents)) {}

    std::string read() const override {
        return contents_;
    }

private:
    std::string contents_;
};

class DataSourceDecorator : public DataSource {
public:
    explicit DataSourceDecorator(std::shared_ptr<DataSource> wrappee) : wrappee_(std::move(wrappee)) {}

protected:
    std::shared_ptr<DataSource> wrappee_;
};

class EncryptionDecorator : public DataSourceDecorator {
public:
    using DataSourceDecorator::DataSourceDecorator;

    std::string read() const override {
        std::string data = wrappee_->read();
        return "<encrypted>" + data + "</encrypted>";
    }
};

class CompressionDecorator : public DataSourceDecorator {
public:
    using DataSourceDecorator::DataSourceDecorator;

    std::string read() const override {
        std::string data = wrappee_->read();
        return "<compressed>" + data + "</compressed>";
    }
};

int main() {
    auto source = std::make_shared<FileDataSource>("salaries.csv");
    auto encrypted = std::make_shared<EncryptionDecorator>(source);
    auto secured = std::make_shared<CompressionDecorator>(encrypted);

    std::cout << secured->read() << '\n';
}
