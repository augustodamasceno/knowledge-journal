package interview.designpatterns.behavioral.state;

interface PlayerState {
    void play(AudioPlayer player);
    void pause(AudioPlayer player);
}

final class AudioPlayer {
    private PlayerState state = new PausedState();
    private String track = "";

    void setState(PlayerState state) {
        this.state = state;
    }

    void setTrack(String track) {
        this.track = track;
        System.out.printf("Current track: %s%n", this.track);
    }

    String track() {
        return track;
    }

    void play() {
        state.play(this);
    }

    void pause() {
        state.pause(this);
    }
}

final class PlayingState implements PlayerState {
    @Override
    public void play(AudioPlayer player) {
        System.out.printf("Already playing %s%n", player.track());
    }

    @Override
    public void pause(AudioPlayer player) {
        System.out.println("Pausing playback");
        player.setState(new PausedState());
    }
}

final class PausedState implements PlayerState {
    @Override
    public void play(AudioPlayer player) {
        System.out.printf("Resuming playback of %s%n", player.track());
        player.setState(new PlayingState());
    }

    @Override
    public void pause(AudioPlayer player) {
        System.out.println("Already paused");
    }
}

public final class StateDemo {
    private StateDemo() {}

    public static void main(String[] args) {
        AudioPlayer player = new AudioPlayer();
        player.setTrack("Track 1");
        player.play();
        player.pause();
        player.play();
    }
}
