using System;

namespace Interview.DesignPatterns.Behavioral.State
{
    public interface IPlayerState
    {
        void Play(AudioPlayer player);
        void Pause(AudioPlayer player);
    }

    public sealed class AudioPlayer
    {
        private IPlayerState _state;
        public string Track { get; private set; } = string.Empty;

        public AudioPlayer()
        {
            _state = new PausedState();
        }

        public void SetState(IPlayerState state)
        {
            _state = state;
        }

        public void SetTrack(string track)
        {
            Track = track;
            Console.WriteLine($"Current track: {Track}");
        }

        public void Play() => _state.Play(this);
        public void Pause() => _state.Pause(this);
    }

    public sealed class PlayingState : IPlayerState
    {
        public void Play(AudioPlayer player)
        {
            Console.WriteLine($"Already playing {player.Track}");
        }

        public void Pause(AudioPlayer player)
        {
            Console.WriteLine("Pausing playback");
            player.SetState(new PausedState());
        }
    }

    public sealed class PausedState : IPlayerState
    {
        public void Play(AudioPlayer player)
        {
            Console.WriteLine($"Resuming playback of {player.Track}");
            player.SetState(new PlayingState());
        }

        public void Pause(AudioPlayer player)
        {
            Console.WriteLine("Already paused");
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var player = new AudioPlayer();
            player.SetTrack("Track 1");
            player.Play();
            player.Pause();
            player.Play();
        }
    }
}
