using System;
using System.Collections.Generic;

namespace Interview.DesignPatterns.Behavioral.Strategy
{
    public interface ISortStrategy
    {
        void Sort(List<int> data);
    }

    public sealed class QuickSortStrategy : ISortStrategy
    {
        public void Sort(List<int> data)
        {
            data.Sort();
            Console.WriteLine("QuickSort applied");
        }
    }

    public sealed class BubbleSortStrategy : ISortStrategy
    {
        public void Sort(List<int> data)
        {
            var n = data.Count;
            var swapped = true;
            while (swapped)
            {
                swapped = false;
                for (var i = 1; i < n; i++)
                {
                    if (data[i - 1] > data[i])
                    {
                        (data[i - 1], data[i]) = (data[i], data[i - 1]);
                        swapped = true;
                    }
                }
                n--;
            }
            Console.WriteLine("BubbleSort applied");
        }
    }

    public sealed class Sorter
    {
        private ISortStrategy _strategy;

        public Sorter(ISortStrategy strategy)
        {
            _strategy = strategy;
        }

        public void SetStrategy(ISortStrategy strategy)
        {
            _strategy = strategy;
        }

        public void Sort(List<int> data)
        {
            _strategy.Sort(data);
        }
    }

    public static class Demo
    {
        public static void Main()
        {
            var numbers = new List<int> { 5, 3, 8, 1, 2 };
            var sorter = new Sorter(new BubbleSortStrategy());
            sorter.Sort(numbers);
            Console.WriteLine(string.Join(" ", numbers));

            numbers = new List<int> { 5, 3, 8, 1, 2 };
            sorter.SetStrategy(new QuickSortStrategy());
            sorter.Sort(numbers);
            Console.WriteLine(string.Join(" ", numbers));
        }
    }
}
