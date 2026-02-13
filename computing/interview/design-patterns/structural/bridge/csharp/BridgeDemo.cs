using System;

namespace Interview.DesignPatterns.Structural.Bridge
{
    public interface IRenderer
    {
        void RenderCircle(double radius);
    }

    public sealed class VectorRenderer : IRenderer
    {
        public void RenderCircle(double radius) => Console.WriteLine($"Vector circle radius={radius}");
    }

    public sealed class RasterRenderer : IRenderer
    {
        public void RenderCircle(double radius) => Console.WriteLine($"Raster circle radius={radius}");
    }

    public abstract class Shape
    {
        protected Shape(IRenderer renderer)
        {
            Renderer = renderer;
        }

        protected IRenderer Renderer { get; }
        public abstract void Draw();
    }

    public sealed class Circle : Shape
    {
        private readonly double _radius;

        public Circle(IRenderer renderer, double radius) : base(renderer)
        {
            _radius = radius;
        }

        public override void Draw()
        {
            Renderer.RenderCircle(_radius);
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var vectorRenderer = new VectorRenderer();
            var rasterRenderer = new RasterRenderer();

            Shape vectorCircle = new Circle(vectorRenderer, 2.5);
            Shape rasterCircle = new Circle(rasterRenderer, 2.5);

            vectorCircle.Draw();
            rasterCircle.Draw();
        }
    }
}
