package interview.designpatterns.behavioral.strategy;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

interface SortStrategy {
    void sort(List<Integer> data);
}

final class QuickSortStrategy implements SortStrategy {
    @Override
    public void sort(List<Integer> data) {
        Collections.sort(data);
        System.out.println("QuickSort applied");
    }
}

final class BubbleSortStrategy implements SortStrategy {
    @Override
    public void sort(List<Integer> data) {
        boolean swapped;
        int n = data.size();
        do {
            swapped = false;
            for (int i = 1; i < n; i++) {
                if (data.get(i - 1) > data.get(i)) {
                    int temp = data.get(i - 1);
                    data.set(i - 1, data.get(i));
                    data.set(i, temp);
                    swapped = true;
                }
            }
            n--;
        } while (swapped);
        System.out.println("BubbleSort applied");
    }
}

final class Sorter {
    private SortStrategy strategy;

    Sorter(SortStrategy strategy) {
        this.strategy = strategy;
    }

    void setStrategy(SortStrategy strategy) {
        this.strategy = strategy;
    }

    void sort(List<Integer> data) {
        strategy.sort(data);
    }
}

public final class StrategyDemo {
    private StrategyDemo() {}

    public static void main(String[] args) {
        List<Integer> numbers = new ArrayList<>(List.of(5, 3, 8, 1, 2));
        Sorter sorter = new Sorter(new BubbleSortStrategy());
        sorter.sort(numbers);
        System.out.println(numbers);

        numbers = new ArrayList<>(List.of(5, 3, 8, 1, 2));
        sorter.setStrategy(new QuickSortStrategy());
        sorter.sort(numbers);
        System.out.println(numbers);
    }
}
