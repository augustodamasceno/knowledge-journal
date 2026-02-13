package interview.designpatterns.behavioral.iterator;

import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.concurrent.CopyOnWriteArrayList;

final class Playlist implements Iterable<String> {
    private final List<String> tracks = new CopyOnWriteArrayList<>();

    void addTrack(String name) {
        tracks.add(name);
    }

    @Override
    public Iterator<String> iterator() {
        return new PlaylistIterator(tracks);
    }

    private static final class PlaylistIterator implements Iterator<String> {
        private final List<String> tracks;
        private int index;

        PlaylistIterator(List<String> tracks) {
            this.tracks = tracks;
        }

        @Override
        public boolean hasNext() {
            return index < tracks.size();
        }

        @Override
        public String next() {
            if (!hasNext()) {
                throw new NoSuchElementException();
            }
            return tracks.get(index++);
        }
    }
}

public final class IteratorDemo {
    private IteratorDemo() {}

    public static void main(String[] args) {
        Playlist playlist = new Playlist();
        playlist.addTrack("Intro");
        playlist.addTrack("Theme");
        playlist.addTrack("Outro");

        for (String track : playlist) {
            System.out.printf("Track: %s%n", track);
        }
    }
}
