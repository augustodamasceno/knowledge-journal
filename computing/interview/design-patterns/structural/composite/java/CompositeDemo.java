package interview.designpatterns.structural.composite;

import java.util.ArrayList;
import java.util.List;

abstract class FileSystemEntry {
    private final String name;

    FileSystemEntry(String name) {
        this.name = name;
    }

    protected String name() {
        return name;
    }

    abstract void print(int indentLevel);

    protected void indent(int level) {
        for (int i = 0; i < level; i++) {
            System.out.print("  ");
        }
    }
}

final class FileEntry extends FileSystemEntry {
    FileEntry(String name) {
        super(name);
    }

    @Override
    void print(int indentLevel) {
        indent(indentLevel);
        System.out.printf("File: %s%n", name());
    }
}

final class DirectoryEntry extends FileSystemEntry {
    private final List<FileSystemEntry> children = new ArrayList<>();

    DirectoryEntry(String name) {
        super(name);
    }

    void add(FileSystemEntry entry) {
        children.add(entry);
    }

    @Override
    void print(int indentLevel) {
        indent(indentLevel);
        System.out.printf("Dir: %s%n", name());
        for (FileSystemEntry child : children) {
            child.print(indentLevel + 1);
        }
    }
}

public final class CompositeDemo {
    private CompositeDemo() {}

    public static void main(String[] args) {
        DirectoryEntry root = new DirectoryEntry("root");
        DirectoryEntry docs = new DirectoryEntry("docs");
        FileEntry img = new FileEntry("image.png");

        docs.add(new FileEntry("resume.pdf"));
        root.add(docs);
        root.add(img);

        root.print(0);
    }
}
