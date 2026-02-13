using System;
using System.Collections.Generic;

namespace Interview.DesignPatterns.Behavioral.Command
{
    public sealed class Editor
    {
        public string Content { get; private set; } = string.Empty;

        public void Append(string text)
        {
            Content += text;
        }

        public void RemoveLast(int length)
        {
            if (length <= Content.Length)
            {
                Content = Content[..^length];
            }
        }
    }

    public interface ICommand
    {
        void Execute();
        void Undo();
    }

    public sealed class AppendCommand : ICommand
    {
        private readonly Editor _editor;
        private readonly string _text;

        public AppendCommand(Editor editor, string text)
        {
            _editor = editor;
            _text = text;
        }

        public void Execute()
        {
            _editor.Append(_text);
        }

        public void Undo()
        {
            _editor.RemoveLast(_text.Length);
        }
    }

    public sealed class Invoker
    {
        private readonly Stack<ICommand> _history = new();

        public void RunCommand(ICommand command)
        {
            command.Execute();
            _history.Push(command);
        }

        public void UndoLast()
        {
            if (_history.Count == 0)
            {
                Console.WriteLine("Nothing to undo");
                return;
            }

            var command = _history.Pop();
            command.Undo();
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var editor = new Editor();
            var invoker = new Invoker();

            invoker.RunCommand(new AppendCommand(editor, "Hello"));
            invoker.RunCommand(new AppendCommand(editor, " World"));
            Console.WriteLine($"Content: {editor.Content}");

            invoker.UndoLast();
            Console.WriteLine($"After undo: {editor.Content}");
        }
    }
}
