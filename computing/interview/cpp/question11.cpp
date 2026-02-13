#include <atomic>
#include <iostream>
#include <thread>

std::atomic<bool> ready{false};
std::atomic<int> data{0};

void producer() {
    data.store(42, std::memory_order_relaxed);
    ready.store(true, std::memory_order_release);
}

void consumer() {
    while (!ready.load(std::memory_order_acquire)) {
        std::this_thread::yield();
    }
    std::cout << "observed: " << data.load(std::memory_order_relaxed) << '\n';
}

int main() {
    std::thread t1(producer);
    std::thread t2(consumer);
    t1.join();
    t2.join();
}
