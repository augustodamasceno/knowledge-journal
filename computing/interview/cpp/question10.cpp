#include <chrono>
#include <iostream>
#include <stop_token>
#include <thread>

void worker(std::stop_token stop, int id) {
    while (!stop.stop_requested()) {
        std::cout << "worker " << id << " tick\n";
        std::this_thread::sleep_for(std::chrono::milliseconds(50));
    }
    std::cout << "worker " << id << " stopping\n";
}

int main() {
    std::jthread producer(worker, 1);

    std::this_thread::sleep_for(std::chrono::milliseconds(130));
    producer.request_stop();

    // std::jthread joins automatically in its destructor.
}
