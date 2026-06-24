class Parser {
    using ll = long long;

    string s;
    size_t i = 0;

    void skipSpaces() {
        while (i < s.size() && s[i] == ' ') {
            i++;
        }
    }

    bool hasMore() {
        skipSpaces();
        return i < s.size();
    }

    char peek() {
        skipSpaces();
        return s[i];
    }

    char consume() {
        skipSpaces();
        return s[i++];
    }

    ll number() {
        skipSpaces();

        ll n = 0;

        while (i < s.size() && isdigit(s[i])) {
            n = n * 10 + (s[i] - '0');
            i++;
        }

        return n;
    }

    ll factor() {
        skipSpaces();

        if (peek() == '+') {
            consume();
            return factor();
        }

        if (peek() == '-') {
            consume();
            return -factor();
        }

        if (peek() == '(') {
            consume();          // '('
            ll val = expr();
            consume();          // ')'
            return val;
        }

        return number();
    }

    ll term() {
        ll result = factor();

        while (hasMore() && (peek() == '*' || peek() == '/')) {
            char op = consume();
            ll right = factor();

            if (op == '*') {
                result *= right;
            } else {
                result /= right;
            }
        }

        return result;
    }

    ll expr() {
        ll result = term();

        while (hasMore() && (peek() == '+' || peek() == '-')) {
            char op = consume();
            ll right = term();

            if (op == '+') {
                result += right;
            } else {
                result -= right;
            }
        }

        return result;
    }

public:
    Parser(const string& expression) : s(expression) {}

    ll eval() {
        return expr();
    }
};

class Solution {
public:
    int calculate(string s) {
        Parser p(s);
        return (int)p.eval();
    }
};
