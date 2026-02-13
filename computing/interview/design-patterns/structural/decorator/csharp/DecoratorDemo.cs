using System;

namespace Interview.DesignPatterns.Structural.Decorator
{
    public interface IDataSource
    {
        string Read();
    }

    public sealed class FileDataSource : IDataSource
    {
        private readonly string _contents;

        public FileDataSource(string contents)
        {
            _contents = contents;
        }

        public string Read() => _contents;
    }

    public abstract class DataSourceDecorator : IDataSource
    {
        protected DataSourceDecorator(IDataSource wrappee)
        {
            Wrappee = wrappee;
        }

        protected IDataSource Wrappee { get; }
        public abstract string Read();
    }

    public sealed class EncryptionDecorator : DataSourceDecorator
    {
        public EncryptionDecorator(IDataSource wrappee) : base(wrappee)
        {
        }

        public override string Read() => $"<encrypted>{Wrappee.Read()}</encrypted>";
    }

    public sealed class CompressionDecorator : DataSourceDecorator
    {
        public CompressionDecorator(IDataSource wrappee) : base(wrappee)
        {
        }

        public override string Read() => $"<compressed>{Wrappee.Read()}</compressed>";
    }

    public static class Demo
    {
        public static void Main()
        {
            IDataSource source = new FileDataSource("salaries.csv");
            IDataSource encrypted = new EncryptionDecorator(source);
            IDataSource secured = new CompressionDecorator(encrypted);
            Console.WriteLine(secured.Read());
        }
    }
}
