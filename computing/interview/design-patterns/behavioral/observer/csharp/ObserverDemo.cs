using System;
using System.Collections.Generic;

namespace Interview.DesignPatterns.Behavioral.Observer
{
    public interface IWeatherObserver
    {
        void Update(double temperature);
    }

    public sealed class WeatherStation
    {
        private readonly List<IWeatherObserver> _observers = new();
        private double _temperature;

        public void AddObserver(IWeatherObserver observer)
        {
            _observers.Add(observer);
        }

        public void SetTemperature(double temperature)
        {
            _temperature = temperature;
            Notify();
        }

        private void Notify()
        {
            foreach (var observer in _observers)
            {
                observer.Update(_temperature);
            }
        }
    }

    public sealed class DisplayPanel : IWeatherObserver
    {
        private readonly string _name;

        public DisplayPanel(string name)
        {
            _name = name;
        }

        public void Update(double temperature)
        {
            Console.WriteLine($"{_name} temperature updated: {temperature}°C");
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var station = new WeatherStation();
            station.AddObserver(new DisplayPanel("Lobby"));
            station.AddObserver(new DisplayPanel("Server Room"));

            station.SetTemperature(22.5);
            station.SetTemperature(24.0);
        }
    }
}
