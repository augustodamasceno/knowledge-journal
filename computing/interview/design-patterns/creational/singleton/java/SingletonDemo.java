package interview.designpatterns.creational.singleton;

public enum Logger {
    INSTANCE;

    public void log(String message) {
        System.out.printf("[LOG] %s%n", message);
    }

    public static void main(String[] args) {
        Logger.INSTANCE.log("Starting process");
        Logger.INSTANCE.log("Process completed");
    }
}
