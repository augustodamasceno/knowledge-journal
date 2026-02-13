package interview.designpatterns.behavioral.mediator;

import java.util.ArrayList;
import java.util.List;

interface ChatMediator {
    void register(ChatUser user);
    void broadcast(String from, String message);
}

final class ChatRoom implements ChatMediator {
    private final List<ChatUser> users = new ArrayList<>();

    @Override
    public void register(ChatUser user) {
        users.add(user);
    }

    @Override
    public void broadcast(String from, String message) {
        for (ChatUser user : users) {
            if (!user.name().equals(from)) {
                user.receive(from, message);
            }
        }
    }
}

final class ChatUser {
    private final String name;
    private final ChatMediator mediator;

    ChatUser(String name, ChatMediator mediator) {
        this.name = name;
        this.mediator = mediator;
    }

    String name() {
        return name;
    }

    void join() {
        mediator.register(this);
    }

    void send(String message) {
        mediator.broadcast(name, message);
    }

    void receive(String from, String message) {
        System.out.printf("%s received from %s: %s%n", name, from, message);
    }
}

public final class MediatorDemo {
    private MediatorDemo() {}

    public static void main(String[] args) {
        ChatRoom room = new ChatRoom();
        ChatUser alice = new ChatUser("Alice", room);
        ChatUser bob = new ChatUser("Bob", room);
        ChatUser carol = new ChatUser("Carol", room);

        alice.join();
        bob.join();
        carol.join();

        alice.send("Hi everyone!");
        bob.send("Hello Alice!");
    }
}
