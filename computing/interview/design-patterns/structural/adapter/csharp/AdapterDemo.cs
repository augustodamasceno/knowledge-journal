using System;

namespace Interview.DesignPatterns.Structural.Adapter
{
    public interface IShape
    {
        void Draw();
    }

    public sealed class ModernCircle : IShape
    {
        private readonly int _radius;

        public ModernCircle(int radius)
        {
            _radius = radius;
        }

        public void Draw() => Console.WriteLine($"Drawing modern circle r={_radius}");
    }

    public sealed class LegacyRectangle
    {
        private readonly int _x;
        private readonly int _y;
        private readonly int _width;
        private readonly int _height;

        public LegacyRectangle(int x, int y, int width, int height)
        {
            _x = x;
            _y = y;
            _width = width;
            _height = height;
        }

        public void OldDraw()
        {
            Console.WriteLine($"Drawing legacy rectangle at ({_x}, {_y}) size {_width}x{_height}");
        }
    }

    public sealed class RectangleAdapter : IShape
    {
        private readonly LegacyRectangle _adaptee;

        public RectangleAdapter(int x, int y, int width, int height)
        {
            _adaptee = new LegacyRectangle(x, y, width, height);
        }

        public void Draw() => _adaptee.OldDraw();
    }

    public static class Demo
    {
        public static void Main()
        {
            IShape circle = new ModernCircle(5);
            IShape rectangle = new RectangleAdapter(10, 10, 20, 15);

            circle.Draw();
            rectangle.Draw();
        }
    }
}
