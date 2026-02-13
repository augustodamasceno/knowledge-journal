package interview.designpatterns.behavioral.memento;

import java.util.Deque;
import java.util.LinkedList;

final class TextMemento {
    private final String state;

    TextMemento(String state) {
        this.state = state;
    }

    String state() {
        return state;
    }
}

final class TextEditor {
    private final StringBuilder content = new StringBuilder();

    void type(String text) {
        content.append(text);
    }

    TextMemento save() {
        return new TextMemento(content.toString());
    }

    void restore(TextMemento memento) {
        content.setLength(0);
        content.append(memento.state());
    }

    String content() {
        return content.toString();
    }
}

final class History {
    private final Deque<TextMemento> snapshots = new LinkedList<>();

    void push(TextMemento memento) {
        snapshots.push(memento);
    }

    TextMemento pop() {
        if (snapshots.isEmpty()) {
            throw new IllegalStateException("No states saved");
        }
        return snapshots.pop();
    }
}

public final class MementoDemo {
    private MementoDemo() {}

    public static void main(String[] args) {
        TextEditor editor = new TextEditor();
        History history = new History();

        editor.type("Hello");
        history.push(editor.save());

        editor.type(" World");
        System.out.printf("Current: %s%n", editor.content());

        editor.restore(history.pop());
        System.out.printf("After undo: %s%n", editor.content());
    }
}
