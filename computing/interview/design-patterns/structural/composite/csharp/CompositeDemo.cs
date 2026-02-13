using System;
using System.Collections.Generic;

namespace Interview.DesignPatterns.Structural.Composite
{
    public abstract class FileSystemEntry
    {
        protected FileSystemEntry(string name)
        {
            Name = name;
        }

        protected string Name { get; }
        public abstract void Print(int indentLevel);

        protected static void Indent(int level)
        {
            for (var i = 0; i < level; i++)
            {
                Console.Write("  ");
            }
        }
    }

    public sealed class File : FileSystemEntry
    {
        public File(string name) : base(name)
        {
        }

        public override void Print(int indentLevel)
        {
            Indent(indentLevel);
            Console.WriteLine($"File: {Name}");
        }
    }

    public sealed class Directory : FileSystemEntry
    {
        private readonly List<FileSystemEntry> _children = new();

        public Directory(string name) : base(name)
        {
        }

        public void Add(FileSystemEntry entry)
        {
            _children.Add(entry);
        }

        public override void Print(int indentLevel)
        {
            Indent(indentLevel);
            Console.WriteLine($"Dir: {Name}");
            foreach (var child in _children)
            {
                child.Print(indentLevel + 1);
            }
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var root = new Directory("root");
            var docs = new Directory("docs");
            var img = new File("image.png");

            docs.Add(new File("resume.pdf"));
            root.Add(docs);
            root.Add(img);

            root.Print(0);
        }
    }
}
