from __future__ import annotations
from typing import List


class ChatMediator:
    def register(self, user: ChatUser) -> None:
        raise NotImplementedError

    def broadcast(self, from_user: str, message: str) -> None:
        raise NotImplementedError


class ChatRoom(ChatMediator):
    def __init__(self) -> None:
        self._users: List[ChatUser] = []

    def register(self, user: ChatUser) -> None:
        self._users.append(user)

    def broadcast(self, from_user: str, message: str) -> None:
        for user in self._users:
            if user.name != from_user:
                user.receive(from_user, message)


class ChatUser:
    def __init__(self, name: str, mediator: ChatMediator) -> None:
        self.name = name
        self._mediator = mediator

    def join(self) -> None:
        self._mediator.register(self)

    def send(self, message: str) -> None:
        self._mediator.broadcast(self.name, message)

    def receive(self, from_user: str, message: str) -> None:
        print(f"{self.name} received from {from_user}: {message}")


def main() -> None:
    room = ChatRoom()
    alice = ChatUser("Alice", room)
    bob = ChatUser("Bob", room)
    carol = ChatUser("Carol", room)

    alice.join()
    bob.join()
    carol.join()

    alice.send("Hi everyone!")
    bob.send("Hello Alice!")


if __name__ == "__main__":
    main()
