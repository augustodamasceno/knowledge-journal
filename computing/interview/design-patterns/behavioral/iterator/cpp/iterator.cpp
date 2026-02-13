#include <iostream>
#include <string>
#include <vector>

class PlaylistIterator;

class Playlist {
public:
    void add_track(std::string name) {
        tracks_.push_back(std::move(name));
    }

    PlaylistIterator begin() const;
    PlaylistIterator end() const;

    const std::vector<std::string>& tracks() const { return tracks_; }

private:
    std::vector<std::string> tracks_;
};

class PlaylistIterator {
public:
    PlaylistIterator(const Playlist* playlist, std::size_t index)
        : playlist_(playlist), index_(index) {}

    bool operator!=(const PlaylistIterator& other) const {
        return index_ != other.index_ || playlist_ != other.playlist_;
    }

    const std::string& operator*() const {
        return playlist_->tracks()[index_];
    }

    const PlaylistIterator& operator++() {
        ++index_;
        return *this;
    }

private:
    const Playlist* playlist_;
    std::size_t index_;
};

PlaylistIterator Playlist::begin() const {
    return PlaylistIterator(this, 0);
}

PlaylistIterator Playlist::end() const {
    return PlaylistIterator(this, tracks_.size());
}

int main() {
    Playlist playlist;
    playlist.add_track("Intro");
    playlist.add_track("Theme");
    playlist.add_track("Outro");

    for (auto it = playlist.begin(); it != playlist.end(); ++it) {
        std::cout << "Track: " << *it << '\n';
    }
}
