#include <iostream>
#include <memory>
#include <string>

class AudioPlayer;

class PlayerState {
public:
    virtual ~PlayerState() = default;
    virtual void play(AudioPlayer& player) = 0;
    virtual void pause(AudioPlayer& player) = 0;
};

class PlayingState;
class PausedState;

class AudioPlayer {
public:
    AudioPlayer();
    void set_state(std::unique_ptr<PlayerState> state) {
        state_ = std::move(state);
    }

    void play() {
        state_->play(*this);
    }

    void pause() {
        state_->pause(*this);
    }

    void set_track(std::string track) {
        track_ = std::move(track);
        std::cout << "Current track: " << track_ << '\n';
    }

    const std::string& track() const { return track_; }

private:
    std::unique_ptr<PlayerState> state_;
    std::string track_ = "";
};

class PlayingState : public PlayerState {
public:
    void play(AudioPlayer& player) override {
        std::cout << "Already playing " << player.track() << '\n';
    }

    void pause(AudioPlayer& player) override;
};

class PausedState : public PlayerState {
public:
    void play(AudioPlayer& player) override;

    void pause(AudioPlayer& player) override {
        std::cout << "Already paused\n";
    }
};

AudioPlayer::AudioPlayer()
    : state_(std::make_unique<PausedState>()) {}

void PlayingState::pause(AudioPlayer& player) {
    std::cout << "Pausing playback\n";
    player.set_state(std::make_unique<PausedState>());
}

void PausedState::play(AudioPlayer& player) {
    std::cout << "Resuming playback of " << player.track() << '\n';
    player.set_state(std::make_unique<PlayingState>());
}

int main() {
    AudioPlayer player;
    player.set_track("Track 1");
    player.play();
    player.pause();
    player.play();
}
