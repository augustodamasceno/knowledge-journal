#include <iostream>
#include <type_traits>
#include <vector>

// Helper trait to detect value_type member.
template <typename, typename = std::void_t<>>
struct has_value_type : std::false_type {};

template <typename T>
struct has_value_type<T, std::void_t<typename T::value_type>> : std::true_type {};

template <typename T>
using enable_if_has_value_type = std::enable_if_t<has_value_type<T>::value>;

// Enabled only when T exposes value_type, implying it behaves like a container.
template <typename T, typename = enable_if_has_value_type<T>>
void debug_container(const T& container) {
    std::cout << "container elements:";
    for (const auto& element : container) {
        std::cout << ' ' << element;
    }
    std::cout << '\n';
}

// Fallback overload when trait is not satisfied.
template <typename T>
void debug_container(const T&) {
    std::cout << "debug_container: unsupported type\n";
}

int main() {
    std::vector<int> numbers{1, 2, 3};
    debug_container(numbers);

    int notAContainer = 42;
    debug_container(notAContainer);
}
