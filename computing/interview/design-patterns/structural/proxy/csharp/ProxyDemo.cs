using System;

namespace Interview.DesignPatterns.Structural.Proxy
{
    public interface IImage
    {
        void Display();
    }

    public sealed class RealImage : IImage
    {
        private readonly string _filename;

        public RealImage(string filename)
        {
            _filename = filename;
            Console.WriteLine($"Loading image from disk: {_filename}");
        }

        public void Display()
        {
            Console.WriteLine($"Displaying image: {_filename}");
        }
    }

    public sealed class LazyImageProxy : IImage
    {
        private readonly string _filename;
        private RealImage? _realImage;

        public LazyImageProxy(string filename)
        {
            _filename = filename;
        }

        public void Display()
        {
            _realImage ??= new RealImage(_filename);
            _realImage.Display();
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            IImage proxy = new LazyImageProxy("photo.png");
            Console.WriteLine("First display triggers load:");
            proxy.Display();
            Console.WriteLine("Second display reuses loaded image:");
            proxy.Display();
        }
    }
}
