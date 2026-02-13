using System;

namespace Interview.DesignPatterns.Structural.Facade
{
    public sealed class Amplifier
    {
        public void On() => Console.WriteLine("Amplifier on");
        public void SetVolume(int level) => Console.WriteLine($"Amplifier volume {level}");
    }

    public sealed class StreamingPlayer
    {
        public void On() => Console.WriteLine("Player on");
        public void PlayMovie(string title) => Console.WriteLine($"Now playing: {title}");
        public void Stop() => Console.WriteLine("Stopping playback");
    }

    public sealed class Projector
    {
        public void On() => Console.WriteLine("Projector on");
        public void WideScreenMode() => Console.WriteLine("Setting widescreen mode");
    }

    public sealed class HomeTheaterFacade
    {
        private readonly Amplifier _amp;
        private readonly StreamingPlayer _player;
        private readonly Projector _projector;

        public HomeTheaterFacade(Amplifier amp, StreamingPlayer player, Projector projector)
        {
            _amp = amp;
            _player = player;
            _projector = projector;
        }

        public void WatchMovie(string title)
        {
            Console.WriteLine("Get ready to watch a movie...");
            _amp.On();
            _amp.SetVolume(7);
            _projector.On();
            _projector.WideScreenMode();
            _player.On();
            _player.PlayMovie(title);
        }

        public void EndMovie()
        {
            Console.WriteLine("Shutting movie theater down...");
            _player.Stop();
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var theater = new HomeTheaterFacade(new Amplifier(), new StreamingPlayer(), new Projector());
            theater.WatchMovie("Inception");
            theater.EndMovie();
        }
    }
}
