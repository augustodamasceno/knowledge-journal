package interview.designpatterns.behavioral.chainofresponsibility;

enum Severity {
    INFO,
    WARNING,
    ERROR
}

final class LogRecord {
    private final Severity level;
    private final String message;

    LogRecord(Severity level, String message) {
        this.level = level;
        this.message = message;
    }

    Severity level() {
        return level;
    }

    String message() {
        return message;
    }
}

abstract class Logger {
    private Logger next;

    void setNext(Logger next) {
        this.next = next;
    }

    void handle(LogRecord record) {
        if (shouldHandle(record.level())) {
            write(record.message());
        } else if (next != null) {
            next.handle(record);
        } else {
            System.out.printf("No handler for message: %s%n", record.message());
        }
    }

    protected abstract boolean shouldHandle(Severity level);
    protected abstract void write(String message);
}

final class ConsoleLogger extends Logger {
    @Override
    protected boolean shouldHandle(Severity level) {
        return level == Severity.INFO;
    }

    @Override
    protected void write(String message) {
        System.out.printf("Console: %s%n", message);
    }
}

final class FileLogger extends Logger {
    @Override
    protected boolean shouldHandle(Severity level) {
        return level == Severity.WARNING;
    }

    @Override
    protected void write(String message) {
        System.out.printf("File: %s%n", message);
    }
}

final class AlertLogger extends Logger {
    @Override
    protected boolean shouldHandle(Severity level) {
        return level == Severity.ERROR;
    }

    @Override
    protected void write(String message) {
        System.out.printf("Alert: %s%n", message);
    }
}

public final class ChainOfResponsibilityDemo {
    private ChainOfResponsibilityDemo() {}

    public static void main(String[] args) {
        Logger console = new ConsoleLogger();
        Logger file = new FileLogger();
        Logger alert = new AlertLogger();

        console.setNext(file);
        file.setNext(alert);

        console.handle(new LogRecord(Severity.INFO, "Starting system"));
        console.handle(new LogRecord(Severity.WARNING, "Disk space low"));
        console.handle(new LogRecord(Severity.ERROR, "Service offline"));
    }
}
