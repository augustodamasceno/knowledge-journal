using System;

namespace Interview.DesignPatterns.Creational.Singleton
{
    public sealed class Logger
    {
        private static readonly Lazy<Logger> _instance = new(() => new Logger());

        private Logger()
        {
        }

        public static Logger Instance => _instance.Value;

        public void Log(string message)
        {
            Console.WriteLine($"[LOG] {message}");
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            Logger.Instance.Log("Starting process");
            Logger.Instance.Log("Process completed");
        }
    }
}
