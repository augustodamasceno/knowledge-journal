using System;
using System.Collections.Generic;

namespace Interview.DesignPatterns.Behavioral.Memento
{
    public sealed class TextMemento
    {
        public TextMemento(string state)
        {
            State = state;
        }

        public string State { get; }
    }

    public sealed class TextEditor
    {
        public string Content { get; private set; } = string.Empty;

        public void Type(string text)
        {
            Content += text;
        }

        public TextMemento Save() => new(Content);

        public void Restore(TextMemento memento)
        {
            Content = memento.State;
        }
    }

    public sealed class History
    {
        private readonly Stack<TextMemento> _snapshots = new();

        public void Push(TextMemento memento) => _snapshots.Push(memento);

        public TextMemento Pop()
        {
            if (_snapshots.Count == 0)
            {
                throw new InvalidOperationException("No states saved");
            }

            return _snapshots.Pop();
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var editor = new TextEditor();
            var history = new History();

            editor.Type("Hello");
            history.Push(editor.Save());

            editor.Type(" World");
            Console.WriteLine($"Current: {editor.Content}");

            editor.Restore(history.Pop());
            Console.WriteLine($"After undo: {editor.Content}");
        }
    }
}
