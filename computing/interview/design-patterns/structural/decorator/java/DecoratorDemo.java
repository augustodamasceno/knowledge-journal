package interview.designpatterns.structural.decorator;

interface DataSource {
    String read();
}

final class FileDataSource implements DataSource {
    private final String contents;

    FileDataSource(String contents) {
        this.contents = contents;
    }

    @Override
    public String read() {
        return contents;
    }
}

abstract class DataSourceDecorator implements DataSource {
    private final DataSource wrappee;

    protected DataSourceDecorator(DataSource wrappee) {
        this.wrappee = wrappee;
    }

    protected DataSource wrappee() {
        return wrappee;
    }
}

final class EncryptionDecorator extends DataSourceDecorator {
    EncryptionDecorator(DataSource wrappee) {
        super(wrappee);
    }

    @Override
    public String read() {
        return "<encrypted>" + wrappee().read() + "</encrypted>";
    }
}

final class CompressionDecorator extends DataSourceDecorator {
    CompressionDecorator(DataSource wrappee) {
        super(wrappee);
    }

    @Override
    public String read() {
        return "<compressed>" + wrappee().read() + "</compressed>";
    }
}

public final class DecoratorDemo {
    private DecoratorDemo() {}

    public static void main(String[] args) {
        DataSource source = new FileDataSource("salaries.csv");
        DataSource secured = new CompressionDecorator(new EncryptionDecorator(source));
        System.out.println(secured.read());
    }
}
