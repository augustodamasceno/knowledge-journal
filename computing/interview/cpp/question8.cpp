#include <charconv>
#include <iostream>
#include <string>
#include <string_view>
#include <system_error>

#if __has_include(<expected>)
#include <expected>
#define HAS_EXPECTED 1
#endif

#ifndef HAS_EXPECTED
#define HAS_EXPECTED 0
#endif

constexpr int identifier(int seed) {
    if consteval {
        return seed * 10;
    }
    return seed * 2;
}

#if HAS_EXPECTED
std::expected<int, std::string> parse_int(std::string_view text) {
    int value{};
    const auto* begin = text.data();
    const auto* end = begin + text.size();
    auto result = std::from_chars(begin, end, value);
    if (result.ec == std::errc()) {
        return value;
    }
    return std::unexpected("parse failure");
}
#endif

int main() {
    constexpr auto compile_time = identifier(7);
    std::cout << "compile-time id: " << compile_time << '\n';
    std::cout << "runtime id: " << identifier(7) << '\n';

#if HAS_EXPECTED
    if (auto parsed = parse_int("123")) {
        std::cout << "parsed: " << *parsed << '\n';
    } else {
        std::cout << "error: " << parsed.error() << '\n';
    }
#endif
}
