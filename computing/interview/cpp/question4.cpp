#include <iostream>
#include <string>
#include <variant>

// Helper to combine multiple lambdas.
template <typename... Visitors>
struct Overloaded : Visitors... {
    using Visitors::operator()...;
};

template <typename... Visitors>
Overloaded(Visitors...) -> Overloaded<Visitors...>;

using Payment = std::variant<int, double, std::string>;

int main() {
    Payment payment = 42; // cents

    auto handler = Overloaded{
        [](int cents) {
            std::cout << "process cash: " << cents << " cents\n";
        },
        [](double dollars) {
            std::cout << "process card: $" << dollars << '\n';
        },
        [](const std::string& token) {
            std::cout << "process voucher: " << token << '\n';
        }
    };

    std::visit(handler, payment);
    payment = 9.99;
    std::visit(handler, payment);
    payment = std::string("PROMO-42");
    std::visit(handler, payment);
}
