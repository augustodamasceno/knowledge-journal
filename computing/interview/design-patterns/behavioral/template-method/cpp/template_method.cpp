#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>

class DataProcessor {
public:
    virtual ~DataProcessor() = default;

    void process(const std::string& input) {
        std::string cleaned = sanitize(input);
        std::string transformed = transform(cleaned);
        persist(transformed);
    }

protected:
    virtual std::string sanitize(const std::string& input) const {
        std::string result = input;
        result.erase(std::remove_if(result.begin(), result.end(), ::isspace), result.end());
        return result;
    }

    virtual std::string transform(const std::string& sanitized) const = 0;
    virtual void persist(const std::string& transformed) const = 0;
};

class UppercaseProcessor : public DataProcessor {
protected:
    std::string transform(const std::string& sanitized) const override {
        std::string result = sanitized;
        std::transform(result.begin(), result.end(), result.begin(), ::toupper);
        return result;
    }

    void persist(const std::string& transformed) const override {
        std::cout << "Persisting uppercase string: " << transformed << '\n';
    }
};

class HashProcessor : public DataProcessor {
protected:
    std::string transform(const std::string& sanitized) const override {
        std::hash<std::string> hasher;
        return std::to_string(hasher(sanitized));
    }

    void persist(const std::string& transformed) const override {
        std::cout << "Persisting hash: " << transformed << '\n';
    }
};

int main() {
    UppercaseProcessor upper;
    HashProcessor hash;

    upper.process("  Hello Template Method  ");
    hash.process("  Hello Template Method  ");
}
