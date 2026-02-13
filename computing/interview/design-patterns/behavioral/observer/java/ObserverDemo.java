package interview.designpatterns.behavioral.observer;

import java.util.ArrayList;
import java.util.List;

interface WeatherObserver {
    void update(double temperature);
}

final class WeatherStation {
    private final List<WeatherObserver> observers = new ArrayList<>();
    private double temperature;

    void addObserver(WeatherObserver observer) {
        observers.add(observer);
    }

    void setTemperature(double temperature) {
        this.temperature = temperature;
        notifyObservers();
    }

    private void notifyObservers() {
        for (WeatherObserver observer : observers) {
            observer.update(temperature);
        }
    }
}

final class DisplayPanel implements WeatherObserver {
    private final String name;

    DisplayPanel(String name) {
        this.name = name;
    }

    @Override
    public void update(double temperature) {
        System.out.printf("%s temperature updated: %.1f°C%n", name, temperature);
    }
}

public final class ObserverDemo {
    private ObserverDemo() {}

    public static void main(String[] args) {
        WeatherStation station = new WeatherStation();
        station.addObserver(new DisplayPanel("Lobby"));
        station.addObserver(new DisplayPanel("Server Room"));

        station.setTemperature(22.5);
        station.setTemperature(24.0);
    }
}
