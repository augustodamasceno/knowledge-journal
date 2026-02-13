#include <iostream>
#include <memory>
#include <string>
#include <vector>

class WeatherObserver {
public:
    virtual ~WeatherObserver() = default;
    virtual void update(double temperature) = 0;
};

class WeatherStation {
public:
    void add_observer(std::shared_ptr<WeatherObserver> observer) {
        observers_.push_back(std::move(observer));
    }

    void set_temperature(double temperature) {
        temperature_ = temperature;
        notify();
    }

private:
    void notify() const {
        for (const auto& observer : observers_) {
            observer->update(temperature_);
        }
    }

    double temperature_ = 0.0;
    std::vector<std::shared_ptr<WeatherObserver>> observers_;
};

class DisplayPanel : public WeatherObserver {
public:
    explicit DisplayPanel(std::string name) : name_(std::move(name)) {}

    void update(double temperature) override {
        std::cout << name_ << " temperature updated: " << temperature << "°C\n";
    }

private:
    std::string name_;
};

int main() {
    WeatherStation station;
    station.add_observer(std::make_shared<DisplayPanel>("Lobby"));
    station.add_observer(std::make_shared<DisplayPanel>("Server Room"));

    station.set_temperature(22.5);
    station.set_temperature(24.0);
}
