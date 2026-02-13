using System;

namespace Interview.DesignPatterns.Behavioral.ChainOfResponsibility
{
    public enum Severity
    {
        Info,
        Warning,
        Error
    }

    public readonly struct LogRecord
    {
        public LogRecord(Severity level, string message)
        {
            Level = level;
            Message = message;
        }

        public Severity Level { get; }
        public string Message { get; }
    }

    public abstract class Logger
    {
        private Logger? _next;

        public void SetNext(Logger next)
        {
            _next = next;
        }

        public void Handle(LogRecord record)
        {
            if (ShouldHandle(record.Level))
            {
                Write(record.Message);
            }
            else if (_next != null)
            {
                _next.Handle(record);
            }
            else
            {
                Console.WriteLine($"No handler for message: {record.Message}");
            }
        }

        protected abstract bool ShouldHandle(Severity level);
        protected abstract void Write(string message);
    }

    public sealed class ConsoleLogger : Logger
    {
        protected override bool ShouldHandle(Severity level) => level == Severity.Info;
        protected override void Write(string message) => Console.WriteLine($"Console: {message}");
    }

    public sealed class FileLogger : Logger
    {
        protected override bool ShouldHandle(Severity level) => level == Severity.Warning;
        protected override void Write(string message) => Console.WriteLine($"File: {message}");
    }

    public sealed class AlertLogger : Logger
    {
        protected override bool ShouldHandle(Severity level) => level == Severity.Error;
        protected override void Write(string message) => Console.WriteLine($"Alert: {message}");
    }

    public static class Demo
    {
        public static void Main()
        {
            var console = new ConsoleLogger();
            var file = new FileLogger();
            var alert = new AlertLogger();

            console.SetNext(file);
            file.SetNext(alert);

            console.Handle(new LogRecord(Severity.Info, "Starting system"));
            console.Handle(new LogRecord(Severity.Warning, "Disk space low"));
            console.Handle(new LogRecord(Severity.Error, "Service offline"));
        }
    }
}
