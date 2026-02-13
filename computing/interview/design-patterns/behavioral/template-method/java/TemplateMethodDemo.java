package interview.designpatterns.behavioral.templatemethod;

import java.util.Locale;

abstract class DataProcessor {
    public final void process(String input) {
        String sanitized = sanitize(input);
        String transformed = transform(sanitized);
        persist(transformed);
    }

    protected String sanitize(String input) {
        return input.replaceAll("\\s", "");
    }

    protected abstract String transform(String sanitized);
    protected abstract void persist(String transformed);
}

final class UppercaseProcessor extends DataProcessor {
    @Override
    protected String transform(String sanitized) {
        return sanitized.toUpperCase(Locale.ROOT);
    }

    @Override
    protected void persist(String transformed) {
        System.out.printf("Persisting uppercase string: %s%n", transformed);
    }
}

final class HashProcessor extends DataProcessor {
    @Override
    protected String transform(String sanitized) {
        int hash = 17;
        for (char c : sanitized.toCharArray()) {
            hash = hash * 31 + c;
        }
        return Integer.toString(hash);
    }

    @Override
    protected void persist(String transformed) {
        System.out.printf("Persisting hash: %s%n", transformed);
    }
}

public final class TemplateMethodDemo {
    private TemplateMethodDemo() {}

    public static void main(String[] args) {
        DataProcessor upper = new UppercaseProcessor();
        DataProcessor hash = new HashProcessor();

        upper.process("  Hello Template Method  ");
        hash.process("  Hello Template Method  ");
    }
}
