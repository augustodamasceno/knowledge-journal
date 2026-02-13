#include <iostream>
#include <map>
#include <memory>
#include <string>

class Context {
public:
    void assign(const std::string& var, bool value) {
        variables_[var] = value;
    }

    bool lookup(const std::string& var) const {
        auto it = variables_.find(var);
        if (it == variables_.end()) {
            throw std::runtime_error("Variable not found");
        }
        return it->second;
    }

private:
    std::map<std::string, bool> variables_;
};

class Expression {
public:
    virtual ~Expression() = default;
    virtual bool interpret(const Context& context) const = 0;
};

class VariableExpression : public Expression {
public:
    explicit VariableExpression(std::string name) : name_(std::move(name)) {}

    bool interpret(const Context& context) const override {
        return context.lookup(name_);
    }

private:
    std::string name_;
};

class AndExpression : public Expression {
public:
    AndExpression(std::unique_ptr<Expression> left, std::unique_ptr<Expression> right)
        : left_(std::move(left)), right_(std::move(right)) {}

    bool interpret(const Context& context) const override {
        return left_->interpret(context) && right_->interpret(context);
    }

private:
    std::unique_ptr<Expression> left_;
    std::unique_ptr<Expression> right_;
};

class OrExpression : public Expression {
public:
    OrExpression(std::unique_ptr<Expression> left, std::unique_ptr<Expression> right)
        : left_(std::move(left)), right_(std::move(right)) {}

    bool interpret(const Context& context) const override {
        return left_->interpret(context) || right_->interpret(context);
    }

private:
    std::unique_ptr<Expression> left_;
    std::unique_ptr<Expression> right_;
};

class NotExpression : public Expression {
public:
    explicit NotExpression(std::unique_ptr<Expression> operand)
        : operand_(std::move(operand)) {}

    bool interpret(const Context& context) const override {
        return !operand_->interpret(context);
    }

private:
    std::unique_ptr<Expression> operand_;
};

int main() {
    Context context;
    context.assign("x", true);
    context.assign("y", false);

    auto expression = std::make_unique<OrExpression>(
        std::make_unique<AndExpression>(
            std::make_unique<VariableExpression>("x"),
            std::make_unique<VariableExpression>("y")),
        std::make_unique<NotExpression>(std::make_unique<VariableExpression>("y")));

    std::cout << std::boolalpha << "Result: " << expression->interpret(context) << '\n';
}
