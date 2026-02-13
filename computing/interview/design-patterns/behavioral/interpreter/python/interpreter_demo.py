from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    def __init__(self) -> None:
        self._variables: dict[str, bool] = {}

    def assign(self, variable: str, value: bool) -> None:
        self._variables[variable] = value

    def lookup(self, variable: str) -> bool:
        try:
            return self._variables[variable]
        except KeyError as exc:
            raise KeyError("Variable not found") from exc


class Expression(ABC):
    @abstractmethod
    def interpret(self, context: Context) -> bool:
        ...


class VariableExpression(Expression):
    def __init__(self, name: str) -> None:
        self._name = name

    def interpret(self, context: Context) -> bool:
        return context.lookup(self._name)


class AndExpression(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> bool:
        return self._left.interpret(context) and self._right.interpret(context)


class OrExpression(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self._left = left
        self._right = right

    def interpret(self, context: Context) -> bool:
        return self._left.interpret(context) or self._right.interpret(context)


class NotExpression(Expression):
    def __init__(self, operand: Expression) -> None:
        self._operand = operand

    def interpret(self, context: Context) -> bool:
        return not self._operand.interpret(context)


def main() -> None:
    context = Context()
    context.assign("x", True)
    context.assign("y", False)

    expression = OrExpression(
        AndExpression(VariableExpression("x"), VariableExpression("y")),
        NotExpression(VariableExpression("y")),
    )

    print(f"Result: {expression.interpret(context)}")


if __name__ == "__main__":
    main()
