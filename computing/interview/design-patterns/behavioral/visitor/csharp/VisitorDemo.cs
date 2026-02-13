using System;

namespace Interview.DesignPatterns.Behavioral.Visitor
{
    public interface IExpressionVisitor
    {
        void Visit(Number number);
        void Visit(Addition addition);
        void Visit(Multiplication multiplication);
    }

    public abstract class Expression
    {
        public abstract void Accept(IExpressionVisitor visitor);
    }

    public sealed class Number : Expression
    {
        public Number(double value)
        {
            Value = value;
        }

        public double Value { get; }
        public override void Accept(IExpressionVisitor visitor) => visitor.Visit(this);
    }

    public sealed class Addition : Expression
    {
        public Addition(Expression left, Expression right)
        {
            Left = left;
            Right = right;
        }

        public Expression Left { get; }
        public Expression Right { get; }
        public override void Accept(IExpressionVisitor visitor) => visitor.Visit(this);
    }

    public sealed class Multiplication : Expression
    {
        public Multiplication(Expression left, Expression right)
        {
            Left = left;
            Right = right;
        }

        public Expression Left { get; }
        public Expression Right { get; }
        public override void Accept(IExpressionVisitor visitor) => visitor.Visit(this);
    }

    public sealed class Evaluator : IExpressionVisitor
    {
        private double _result;

        public double Result => _result;

        public void Visit(Number number)
        {
            _result = number.Value;
        }

        public void Visit(Addition addition)
        {
            addition.Left.Accept(this);
            var left = _result;
            addition.Right.Accept(this);
            var right = _result;
            _result = left + right;
        }

        public void Visit(Multiplication multiplication)
        {
            multiplication.Left.Accept(this);
            var left = _result;
            multiplication.Right.Accept(this);
            var right = _result;
            _result = left * right;
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            Expression expression = new Addition(
                new Number(2),
                new Multiplication(new Number(3), new Number(4)));

            var evaluator = new Evaluator();
            expression.Accept(evaluator);
            Console.WriteLine($"Result: {evaluator.Result}");
        }
    }
}
