// Stack — using std::stack (adaptor over std::deque by default)
#include <iostream>
#include <stack>
#include <string>

// Classic use-case: balanced parentheses checker
bool isBalanced(const std::string& s) {
    std::stack<char> st;
    for (char c : s) {
        if (c == '(' || c == '[' || c == '{') {
            st.push(c);
        } else if (c == ')' || c == ']' || c == '}') {
            if (st.empty()) return false;
            char top = st.top(); st.pop();
            if ((c == ')' && top != '(') ||
                (c == ']' && top != '[') ||
                (c == '}' && top != '{')) return false;
        }
    }
    return st.empty();
}

int main() {
    std::stack<int> st;
    st.push(1);   // O(1)
    st.push(2);
    st.push(3);

    std::cout << "Top: " << st.top() << "\n";   // 3
    st.pop();                                    // O(1)
    std::cout << "After pop, top: " << st.top() << "\n"; // 2
    std::cout << "Size: " << st.size() << "\n";

    // Balanced parentheses demo
    std::cout << std::boolalpha;
    std::cout << "\"({[]})\" balanced: " << isBalanced("({[]})") << "\n";
    std::cout << "\"({[})\"  balanced: " << isBalanced("({[})")  << "\n";

    return 0;
}
