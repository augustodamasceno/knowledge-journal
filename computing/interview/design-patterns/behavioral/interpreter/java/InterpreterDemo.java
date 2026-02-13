package interview.designpatterns.behavioral.interpreter;

import java.util.HashMap;
import java.util.Map;

final class Context {
    private final Map<String, Boolean> variables = new HashMap<>();

    void assign(String variable, boolean value) {
        variables.put(variable, value);
    }

    boolean lookup(String variable) {
        Boolean value = variables.get(variable);
        if (value == null) {
            throw new IllegalArgumentException("Variable not found");
        }
        return value;
    }
}

interface Expression {
    boolean interpret(Context context);
}

final class VariableExpression implements Expression {
    private final String name;

    VariableExpression(String name) {
        this.name = name;
    }

    @Override
    public boolean interpret(Context context) {
        return context.lookup(name);
    }
}

final class AndExpression implements Expression {
    private final Expression left;
    private final Expression right;

    AndExpression(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public boolean interpret(Context context) {
        return left.interpret(context) && right.interpret(context);
    }
}

final class OrExpression implements Expression {
    private final Expression left;
    private final Expression right;

    OrExpression(Expression left, Expression right) {
        this.left = left;
        this.right = right;
    }

    @Override
    public boolean interpret(Context context) {
        return left.interpret(context) || right.interpret(context);
    }
}

final class NotExpression implements Expression {
    private final Expression operand;

    NotExpression(Expression operand) {
        this.operand = operand;
    }

    @Override
    public boolean interpret(Context context) {
        return !operand.interpret(context);
    }
}

public final class InterpreterDemo {
    private InterpreterDemo() {}

    public static void main(String[] args) {
        Context context = new Context();
        context.assign("x", true);
        context.assign("y", false);

        Expression expression = new OrExpression(
            new AndExpression(new VariableExpression("x"), new VariableExpression("y")),
            new NotExpression(new VariableExpression("y")));

        System.out.printf("Result: %b%n", expression.interpret(context));
    }
}
