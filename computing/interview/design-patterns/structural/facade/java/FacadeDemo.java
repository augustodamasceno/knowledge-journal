package interview.designpatterns.structural.facade;

final class Amplifier {
    void on() {
        System.out.println("Amplifier on");
    }

    void setVolume(int level) {
        System.out.printf("Amplifier volume %d%n", level);
    }
}

final class StreamingPlayer {
    void on() {
        System.out.println("Player on");
    }

    void playMovie(String title) {
        System.out.printf("Now playing: %s%n", title);
    }

    void stop() {
        System.out.println("Stopping playback");
    }
}

final class Projector {
    void on() {
        System.out.println("Projector on");
    }

    void wideScreenMode() {
        System.out.println("Setting widescreen mode");
    }
}

final class HomeTheaterFacade {
    private final Amplifier amp;
    private final StreamingPlayer player;
    private final Projector projector;

    HomeTheaterFacade(Amplifier amp, StreamingPlayer player, Projector projector) {
        this.amp = amp;
        this.player = player;
        this.projector = projector;
    }

    void watchMovie(String title) {
        System.out.println("Get ready to watch a movie...");
        amp.on();
        amp.setVolume(7);
        projector.on();
        projector.wideScreenMode();
        player.on();
        player.playMovie(title);
    }

    void endMovie() {
        System.out.println("Shutting movie theater down...");
        player.stop();
    }
}

public final class FacadeDemo {
    private FacadeDemo() {}

    public static void main(String[] args) {
        HomeTheaterFacade theater = new HomeTheaterFacade(new Amplifier(), new StreamingPlayer(), new Projector());
        theater.watchMovie("Inception");
        theater.endMovie();
    }
}
