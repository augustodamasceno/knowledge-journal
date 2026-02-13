from __future__ import annotations
from __future__ import annotations

from abc import ABC, abstractmethod


class ExpressionVisitor(ABC):
    @abstractmethod
    def visit_number(self, number: NumberLiteral) -> None:
        ...

    @abstractmethod
    def visit_addition(self, addition: Addition) -> None:
        ...

    @abstractmethod
    def visit_multiplication(self, multiplication: Multiplication) -> None:
        ...


class Expression(ABC):
    @abstractmethod
    def accept(self, visitor: ExpressionVisitor) -> None:
        ...


class NumberLiteral(Expression):
    def __init__(self, value: float) -> None:
        self.value = value

    def accept(self, visitor: ExpressionVisitor) -> None:
        visitor.visit_number(self)


class Addition(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def accept(self, visitor: ExpressionVisitor) -> None:
        visitor.visit_addition(self)


class Multiplication(Expression):
    def __init__(self, left: Expression, right: Expression) -> None:
        self.left = left
        self.right = right

    def accept(self, visitor: ExpressionVisitor) -> None:
        visitor.visit_multiplication(self)


class Evaluator(ExpressionVisitor):
    def __init__(self) -> None:
        self.result = 0.0

    def visit_number(self, number: NumberLiteral) -> None:
        self.result = number.value

    def visit_addition(self, addition: Addition) -> None:
        addition.left.accept(self)
        left = self.result
        addition.right.accept(self)
        right = self.result
        self.result = left + right

    def visit_multiplication(self, multiplication: Multiplication) -> None:
        multiplication.left.accept(self)
        left = self.result
        multiplication.right.accept(self)
        right = self.result
        self.result = left * right


def main() -> None:
    expression = Addition(NumberLiteral(2), Multiplication(NumberLiteral(3), NumberLiteral(4)))
    evaluator = Evaluator()
    expression.accept(evaluator)
    print(f"Result: {evaluator.result}")


if __name__ == "__main__":
    main()
