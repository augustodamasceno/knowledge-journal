using System;
using System.Collections.Generic;

namespace Interview.DesignPatterns.Creational.Builder
{
    public sealed class Meal
    {
        private readonly List<string> _items;
        private readonly int _calories;

        public Meal(IEnumerable<string> items, int calories)
        {
            _items = new List<string>(items);
            _calories = calories;
        }

        public void Describe()
        {
            Console.WriteLine($"Meal: {string.Join(" ", _items)} ({_calories} kcal)");
        }
    }

    public sealed class MealBuilder
    {
        private readonly List<string> _items = new();
        private int _calories;

        public MealBuilder AddMain(string name, int calories)
        {
            _items.Add(name);
            _calories += calories;
            return this;
        }

        public MealBuilder AddSide(string name, int calories)
        {
            _items.Add(name);
            _calories += calories;
            return this;
        }

        public MealBuilder AddDrink(string name, int calories)
        {
            _items.Add(name);
            _calories += calories;
            return this;
        }

        public Meal Build()
        {
            var meal = new Meal(_items, _calories);
            _items.Clear();
            _calories = 0;
            return meal;
        }
    }

    public sealed class MealDirector
    {
        public Meal CreateHighProtein(MealBuilder builder) => builder
            .AddMain("Grilled chicken", 400)
            .AddSide("Quinoa", 180)
            .AddDrink("Protein shake", 220)
            .Build();

        public Meal CreateVegetarian(MealBuilder builder) => builder
            .AddMain("Tofu stir-fry", 320)
            .AddSide("Salad", 90)
            .AddDrink("Green tea", 0)
            .Build();
    }

    public static class Demo
    {
        public static void Main()
        {
            var builder = new MealBuilder();
            var director = new MealDirector();

            director.CreateHighProtein(builder).Describe();
            director.CreateVegetarian(builder).Describe();
        }
    }
}
