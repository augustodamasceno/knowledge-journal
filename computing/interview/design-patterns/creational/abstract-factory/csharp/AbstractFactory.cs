using System;

namespace Interview.DesignPatterns.Creational.AbstractFactory
{
    public interface IButton
    {
        void Render();
    }

    public interface ICheckbox
    {
        void Toggle();
    }

    public interface IGuiFactory
    {
        IButton CreateButton();
        ICheckbox CreateCheckbox();
    }

    public sealed class WindowsButton : IButton
    {
        public void Render() => Console.WriteLine("Rendering Windows button");
    }

    public sealed class WindowsCheckbox : ICheckbox
    {
        public void Toggle() => Console.WriteLine("Toggling Windows checkbox");
    }

    public sealed class WindowsFactory : IGuiFactory
    {
        public IButton CreateButton() => new WindowsButton();
        public ICheckbox CreateCheckbox() => new WindowsCheckbox();
    }

    public sealed class MacButton : IButton
    {
        public void Render() => Console.WriteLine("Rendering macOS button");
    }

    public sealed class MacCheckbox : ICheckbox
    {
        public void Toggle() => Console.WriteLine("Toggling macOS checkbox");
    }

    public sealed class MacFactory : IGuiFactory
    {
        public IButton CreateButton() => new MacButton();
        public ICheckbox CreateCheckbox() => new MacCheckbox();
    }

    public sealed class Application
    {
        private readonly IGuiFactory _factory;

        public Application(IGuiFactory factory)
        {
            _factory = factory;
        }

        public void PaintUi()
        {
            var button = _factory.CreateButton();
            var checkbox = _factory.CreateCheckbox();
            button.Render();
            checkbox.Toggle();
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var windowsApp = new Application(new WindowsFactory());
            windowsApp.PaintUi();

            var macApp = new Application(new MacFactory());
            macApp.PaintUi();
        }
    }
}
