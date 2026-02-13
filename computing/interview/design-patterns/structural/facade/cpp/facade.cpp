#include <iostream>

class Amplifier {
public:
    void on() const { std::cout << "Amplifier on\n"; }
    void set_volume(int level) const { std::cout << "Amplifier volume " << level << "\n"; }
};

class StreamingPlayer {
public:
    void on() const { std::cout << "Player on\n"; }
    void play_movie(const std::string& title) const { std::cout << "Now playing: " << title << "\n"; }
    void stop() const { std::cout << "Stopping playback\n"; }
};

class Projector {
public:
    void on() const { std::cout << "Projector on\n"; }
    void wide_screen_mode() const { std::cout << "Setting widescreen mode\n"; }
};

class HomeTheaterFacade {
public:
    HomeTheaterFacade(Amplifier amp, StreamingPlayer player, Projector projector)
        : amp_(amp), player_(player), projector_(projector) {}

    void watch_movie(const std::string& title) const {
        std::cout << "Get ready to watch a movie...\n";
        amp_.on();
        amp_.set_volume(7);
        projector_.on();
        projector_.wide_screen_mode();
        player_.on();
        player_.play_movie(title);
    }

    void end_movie() const {
        std::cout << "Shutting movie theater down...\n";
        player_.stop();
    }

private:
    Amplifier amp_;
    StreamingPlayer player_;
    Projector projector_;
};

int main() {
    HomeTheaterFacade theater(Amplifier{}, StreamingPlayer{}, Projector{});
    theater.watch_movie("Inception");
    theater.end_movie();
}
