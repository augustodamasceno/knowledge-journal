package interview.designpatterns.behavioral.visitor;

interface ExpressionVisitor {
    void visit(NumberLiteral number);
    void visit(Addition addition);
    void visit(Multiplication multiplication);
}

abstract class Expression {
    abstract void accept(ExpressionVisitor visitor);
}

final class NumberLiteral extends Expression {
    private final double value;

    NumberLiteral(double value) {
        this.value = value;
    }

    double value() {
        return value;
    }

    @Override
    void accept(ExpressionVisitor visitor) {
        visitor.visit(this);
    }
}

final class Addition extends Expression {
    private final Expression left;
    private final Expression right;

    Addition(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }

    Expression left() {
        return left;
    }

    Expression right() {
        return right;
    }

    @Override
    void accept(ExpressionVisitor visitor) {
        visitor.visit(this);
    }
}

final class Multiplication extends Expression {
    private final Expression left;
    private final Expression right;

    Multiplication(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }

    Expression left() {
        return left;
    }

    Expression right() {
        return right;
    }

    @Override
    void accept(ExpressionVisitor visitor) {
        visitor.visit(this);
    }
}

final class Evaluator implements ExpressionVisitor {
    private double result;

    double result() {
        return result;
    }

    @Override
    public void visit(NumberLiteral number) {
        result = number.value();
    }

    @Override
    public void visit(Addition addition) {
        addition.left().accept(this);
        double left = result;
        addition.right().accept(this);
        double right = result;
        result = left + right;
    }

    @Override
    public void visit(Multiplication multiplication) {
        multiplication.left().accept(this);
        double left = result;
        multiplication.right().accept(this);
        double right = result;
        result = left * right;
    }
}

public final class VisitorDemo {
    private VisitorDemo() {}

    public static void main(String[] args) {
        Expression expression = new Addition(
            new NumberLiteral(2),
            new Multiplication(new NumberLiteral(3), new NumberLiteral(4)));

        Evaluator evaluator = new Evaluator();
        expression.accept(evaluator);
        System.out.printf("Result: %.1f%n", evaluator.result());
    }
}
