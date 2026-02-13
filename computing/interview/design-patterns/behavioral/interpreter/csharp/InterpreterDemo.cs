using System;
using System.Collections.Generic;

namespace Interview.DesignPatterns.Behavioral.Interpreter
{
    public sealed class Context
    {
        private readonly Dictionary<string, bool> _variables = new();

        public void Assign(string variable, bool value)
        {
            _variables[variable] = value;
        }

        public bool Lookup(string variable)
        {
            if (!_variables.TryGetValue(variable, out var value))
            {
                throw new InvalidOperationException("Variable not found");
            }

            return value;
        }
    }

    public interface IExpression
    {
        bool Interpret(Context context);
    }

    public sealed class VariableExpression : IExpression
    {
        private readonly string _name;

        public VariableExpression(string name)
        {
            _name = name;
        }

        public bool Interpret(Context context) => context.Lookup(_name);
    }

    public sealed class AndExpression : IExpression
    {
        private readonly IExpression _left;
        private readonly IExpression _right;

        public AndExpression(IExpression left, IExpression right)
        {
            _left = left;
            _right = right;
        }

        public bool Interpret(Context context) => _left.Interpret(context) && _right.Interpret(context);
    }

    public sealed class OrExpression : IExpression
    {
        private readonly IExpression _left;
        private readonly IExpression _right;

        public OrExpression(IExpression left, IExpression right)
        {
            _left = left;
            _right = right;
        }

        public bool Interpret(Context context) => _left.Interpret(context) || _right.Interpret(context);
    }

    public sealed class NotExpression : IExpression
    {
        private readonly IExpression _operand;

        public NotExpression(IExpression operand)
        {
            _operand = operand;
        }

        public bool Interpret(Context context) => !_operand.Interpret(context);
    }

    public static class Demo
    {
        public static void Main()
        {
            var context = new Context();
            context.Assign("x", true);
            context.Assign("y", false);

            IExpression expression = new OrExpression(
                new AndExpression(new VariableExpression("x"), new VariableExpression("y")),
                new NotExpression(new VariableExpression("y")));

            Console.WriteLine($"Result: {expression.Interpret(context)}");
        }
    }
}
