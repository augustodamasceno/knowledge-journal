#include <iostream>
#include <memory>
#include <string>
#include <vector>

class ChatUser;

class ChatMediator {
public:
    virtual ~ChatMediator() = default;
    virtual void register_user(ChatUser* user) = 0;
    virtual void broadcast(const std::string& from, const std::string& message) const = 0;
};

class ChatUser {
public:
    ChatUser(std::string name, ChatMediator& mediator)
        : name_(std::move(name)), mediator_(mediator) {}

    void join() {
        mediator_.register_user(this);
    }

    void send(const std::string& message) const {
        mediator_.broadcast(name_, message);
    }

    void receive(const std::string& from, const std::string& message) const {
        std::cout << name_ << " received from " << from << ": " << message << '\n';
    }

    const std::string& name() const { return name_; }

private:
    std::string name_;
    ChatMediator& mediator_;
};

class ChatRoom : public ChatMediator {
public:
    void register_user(ChatUser* user) override {
        users_.push_back(user);
    }

    void broadcast(const std::string& from, const std::string& message) const override {
        for (auto* user : users_) {
            if (user->name() != from) {
                user->receive(from, message);
            }
        }
    }

private:
    std::vector<ChatUser*> users_;
};

int main() {
    ChatRoom room;
    ChatUser alice("Alice", room);
    ChatUser bob("Bob", room);
    ChatUser carol("Carol", room);

    alice.join();
    bob.join();
    carol.join();

    alice.send("Hi everyone!");
    bob.send("Hello Alice!");
}
