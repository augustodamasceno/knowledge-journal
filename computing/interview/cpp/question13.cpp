#include <iostream>
#include <memory_resource>
#include <string>
#include <vector>

int main() {
    std::byte buffer[1024];
    std::pmr::monotonic_buffer_resource pool(buffer, sizeof(buffer));

    std::pmr::vector<std::pmr::string> log{&pool};
    log.emplace_back("connect client");
    log.emplace_back("fetch data");
    log.emplace_back("disconnect");

    for (const auto& entry : log) {
        std::cout << entry << '\n';
    }

    std::cout << "remaining pool: " << pool.remaining_storage() << " bytes\n";
}
