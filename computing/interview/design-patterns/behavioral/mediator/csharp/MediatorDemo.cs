using System;
using System.Collections.Generic;

namespace Interview.DesignPatterns.Behavioral.Mediator
{
    public interface IChatMediator
    {
        void Register(ChatUser user);
        void Broadcast(string from, string message);
    }

    public sealed class ChatRoom : IChatMediator
    {
        private readonly List<ChatUser> _users = new();

        public void Register(ChatUser user)
        {
            _users.Add(user);
        }

        public void Broadcast(string from, string message)
        {
            foreach (var user in _users)
            {
                if (!user.Name.Equals(from, StringComparison.Ordinal))
                {
                    user.Receive(from, message);
                }
            }
        }
    }

    public sealed class ChatUser
    {
        private readonly IChatMediator _mediator;

        public ChatUser(string name, IChatMediator mediator)
        {
            Name = name;
            _mediator = mediator;
        }

        public string Name { get; }

        public void Join()
        {
            _mediator.Register(this);
        }

        public void Send(string message)
        {
            _mediator.Broadcast(Name, message);
        }

        public void Receive(string from, string message)
        {
            Console.WriteLine($"{Name} received from {from}: {message}");
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var room = new ChatRoom();
            var alice = new ChatUser("Alice", room);
            var bob = new ChatUser("Bob", room);
            var carol = new ChatUser("Carol", room);

            alice.Join();
            bob.Join();
            carol.Join();

            alice.Send("Hi everyone!");
            bob.Send("Hello Alice!");
        }
    }
}
