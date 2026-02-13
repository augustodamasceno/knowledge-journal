using System;
using System.Collections.Generic;

namespace Interview.DesignPatterns.Creational.Prototype
{
    public abstract class DiagramNode
    {
        protected DiagramNode(string label)
        {
            Label = label;
        }

        public string Label { get; }
        public abstract DiagramNode Clone();
        public abstract void Render();
    }

    public sealed class CircleNode : DiagramNode
    {
        private readonly double _radius;

        public CircleNode(string label, double radius) : base(label)
        {
            _radius = radius;
        }

        public override DiagramNode Clone() => new CircleNode(Label, _radius);

        public override void Render()
        {
            Console.WriteLine($"Circle({Label}, r={_radius})");
        }
    }

    public sealed class RectangleNode : DiagramNode
    {
        private readonly double _width;
        private readonly double _height;

        public RectangleNode(string label, double width, double height) : base(label)
        {
            _width = width;
            _height = height;
        }

        public override DiagramNode Clone() => new RectangleNode(Label, _width, _height);

        public override void Render()
        {
            Console.WriteLine($"Rectangle({Label}, {_width}x{_height})");
        }
    }

    public sealed class PrototypeRegistry
    {
        private readonly Dictionary<string, DiagramNode> _prototypes = new();

        public void Register(string name, DiagramNode prototype)
        {
            _prototypes[name] = prototype;
        }

        public DiagramNode Create(string name)
        {
            if (!_prototypes.TryGetValue(name, out var prototype))
            {
                throw new InvalidOperationException("Prototype not found");
            }

            return prototype.Clone();
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var registry = new PrototypeRegistry();
            registry.Register("small_circle", new CircleNode("Small", 1.0));
            registry.Register("wide_rect", new RectangleNode("Wide", 3.0, 1.0));

            var node1 = registry.Create("small_circle");
            var node2 = registry.Create("wide_rect");

            node1.Render();
            node2.Render();
        }
    }
}
