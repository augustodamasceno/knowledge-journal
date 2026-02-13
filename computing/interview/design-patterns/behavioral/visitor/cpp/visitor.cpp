#include <iostream>
#include <memory>
#include <vector>

class Number;
class Addition;
class Multiplication;

class ExpressionVisitor {
public:
    virtual ~ExpressionVisitor() = default;
    virtual void visit(const Number& number) = 0;
    virtual void visit(const Addition& addition) = 0;
    virtual void visit(const Multiplication& multiplication) = 0;
};

class Expression {
public:
    virtual ~Expression() = default;
    virtual void accept(ExpressionVisitor& visitor) const = 0;
};

class Number : public Expression {
public:
    explicit Number(double value) : value_(value) {}
    double value() const { return value_; }

    void accept(ExpressionVisitor& visitor) const override {
        visitor.visit(*this);
    }

private:
    double value_;
};

class Addition : public Expression {
public:
    Addition(std::unique_ptr<Expression> left, std::unique_ptr<Expression> right)
        : left_(std::move(left)), right_(std::move(right)) {}

    const Expression& left() const { return *left_; }
    const Expression& right() const { return *right_; }

    void accept(ExpressionVisitor& visitor) const override {
        visitor.visit(*this);
    }

private:
    std::unique_ptr<Expression> left_;
    std::unique_ptr<Expression> right_;
};

class Multiplication : public Expression {
public:
    Multiplication(std::unique_ptr<Expression> left, std::unique_ptr<Expression> right)
        : left_(std::move(left)), right_(std::move(right)) {}

    const Expression& left() const { return *left_; }
    const Expression& right() const { return *right_; }

    void accept(ExpressionVisitor& visitor) const override {
        visitor.visit(*this);
    }

private:
    std::unique_ptr<Expression> left_;
    std::unique_ptr<Expression> right_;
};

class Evaluator : public ExpressionVisitor {
public:
    double result() const {
        if (result_stack_.empty()) {
            return 0.0;
        }
        return result_stack_.back();
    }

    void visit(const Number& number) override {
        result_stack_.push_back(number.value());
    }

    void visit(const Addition& addition) override {
        addition.left().accept(*this);
        double left_value = pop();
        addition.right().accept(*this);
        double right_value = pop();
        result_stack_.push_back(left_value + right_value);
    }

    void visit(const Multiplication& multiplication) override {
        multiplication.left().accept(*this);
        double left_value = pop();
        multiplication.right().accept(*this);
        double right_value = pop();
        result_stack_.push_back(left_value * right_value);
    }

private:
    double pop() {
        double value = result_stack_.back();
        result_stack_.pop_back();
        return value;
    }

    std::vector<double> result_stack_;
};

int main() {
    auto expression = std::make_unique<Addition>(
        std::make_unique<Number>(2),
        std::make_unique<Multiplication>(
            std::make_unique<Number>(3),
            std::make_unique<Number>(4)));

    Evaluator evaluator;
    expression->accept(evaluator);
    std::cout << "Result: " << evaluator.result() << '\n';
}
