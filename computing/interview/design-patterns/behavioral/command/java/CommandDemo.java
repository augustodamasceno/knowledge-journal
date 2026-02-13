package interview.designpatterns.behavioral.command;

import java.util.Deque;
import java.util.LinkedList;

final class Editor {
    private final StringBuilder content = new StringBuilder();

    void append(String text) {
        content.append(text);
    }

    void removeLast(int length) {
        int start = Math.max(content.length() - length, 0);
        content.delete(start, content.length());
    }

    String content() {
        return content.toString();
    }
}

interface Command {
    void execute();
    void undo();
}

final class AppendCommand implements Command {
    private final Editor editor;
    private final String text;

    AppendCommand(Editor editor, String text) {
        this.editor = editor;
        this.text = text;
    }

    @Override
    public void execute() {
        editor.append(text);
    }

    @Override
    public void undo() {
        editor.removeLast(text.length());
    }
}

final class Invoker {
    private final Deque<Command> history = new LinkedList<>();

    void runCommand(Command command) {
        command.execute();
        history.push(command);
    }

    void undoLast() {
        if (history.isEmpty()) {
            System.out.println("Nothing to undo");
            return;
        }
        Command command = history.pop();
        command.undo();
    }
}

public final class CommandDemo {
    private CommandDemo() {}

    public static void main(String[] args) {
        Editor editor = new Editor();
        Invoker invoker = new Invoker();

        invoker.runCommand(new AppendCommand(editor, "Hello"));
        invoker.runCommand(new AppendCommand(editor, " World"));
        System.out.printf("Content: %s%n", editor.content());

        invoker.undoLast();
        System.out.printf("After undo: %s%n", editor.content());
    }
}
