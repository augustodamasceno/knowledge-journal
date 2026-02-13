using System;
using System.Collections;
using System.Collections.Generic;

namespace Interview.DesignPatterns.Behavioral.Iterator
{
    public sealed class Playlist : IEnumerable<string>
    {
        private readonly List<string> _tracks = new();

        public void AddTrack(string name)
        {
            _tracks.Add(name);
        }

        public IEnumerator<string> GetEnumerator()
        {
            return new PlaylistEnumerator(_tracks);
        }

        IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();

        private sealed class PlaylistEnumerator : IEnumerator<string>
        {
            private readonly List<string> _tracks;
            private int _index = -1;

            public PlaylistEnumerator(List<string> tracks)
            {
                _tracks = tracks;
            }

            public string Current => _tracks[_index];
            object IEnumerator.Current => Current;

            public bool MoveNext()
            {
                _index++;
                return _index < _tracks.Count;
            }

            public void Reset()
            {
                _index = -1;
            }

            public void Dispose()
            {
            }
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var playlist = new Playlist();
            playlist.AddTrack("Intro");
            playlist.AddTrack("Theme");
            playlist.AddTrack("Outro");

            foreach (var track in playlist)
            {
                Console.WriteLine($"Track: {track}");
            }
        }
    }
}
