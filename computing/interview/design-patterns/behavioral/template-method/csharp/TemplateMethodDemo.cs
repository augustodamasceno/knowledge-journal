using System;
using System.Linq;

namespace Interview.DesignPatterns.Behavioral.TemplateMethod
{
    public abstract class DataProcessor
    {
        public void Process(string input)
        {
            var cleaned = Sanitize(input);
            var transformed = Transform(cleaned);
            Persist(transformed);
        }

        protected virtual string Sanitize(string input)
        {
            return new string(input.Where(c => !char.IsWhiteSpace(c)).ToArray());
        }

        protected abstract string Transform(string sanitized);
        protected abstract void Persist(string transformed);
    }

    public sealed class UppercaseProcessor : DataProcessor
    {
        protected override string Transform(string sanitized) => sanitized.ToUpperInvariant();

        protected override void Persist(string transformed)
        {
            Console.WriteLine($"Persisting uppercase string: {transformed}");
        }
    }

    public sealed class HashProcessor : DataProcessor
    {
        protected override string Transform(string sanitized)
        {
            return sanitized.Aggregate(17, (hash, c) => hash * 31 + c).ToString();
        }

        protected override void Persist(string transformed)
        {
            Console.WriteLine($"Persisting hash: {transformed}");
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            DataProcessor upper = new UppercaseProcessor();
            DataProcessor hash = new HashProcessor();

            upper.Process("  Hello Template Method  ");
            hash.Process("  Hello Template Method  ");
        }
    }
}
