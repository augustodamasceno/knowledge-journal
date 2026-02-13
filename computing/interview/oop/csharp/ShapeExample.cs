using System;
using System.Collections.Generic;

namespace Interview.Oop
{
    public abstract class Shape
    {
        public abstract double Area { get; }
        public abstract void Describe();
    }

    public sealed class Circle : Shape
    {
        private readonly double _radius;

        public Circle(double radius)
        {
            _radius = radius;
        }

        public override double Area => Math.PI * _radius * _radius;

        public override void Describe()
        {
            Console.WriteLine($"Circle radius={_radius} area={Area:0.###}");
        }
    }

    public sealed class Rectangle : Shape
    {
        private readonly double _width;
        private readonly double _height;

        public Rectangle(double width, double height)
        {
            _width = width;
            _height = height;
        }

        public override double Area => _width * _height;

        public override void Describe()
        {
            Console.WriteLine($"Rectangle {_width}x{_height} area={Area:0.###}");
        }
    }

    public static class Program
    {
        public static void Main()
        {
            var shapes = new List<Shape>
            {
                new Circle(2.0),
                new Rectangle(3.0, 4.0)
            };

            foreach (var shape in shapes)
            {
                shape.Describe();
            }
        }
    }
}
