class Parser{
    private:
      size_t index = 0;
      vector<string> tokens{};
      int ans{};

      int apply(const string& opp, int a, int b)
      {
        switch (opp[0]) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/':
                return a / b;
            default:
                return 0;
        }
      }

    public:
        Parser(const std::string& expression): index(0), ans(0) 
        {
            for (char c : expression) {
                if (c == ' ') continue;
                tokens.push_back(string(1, c));
            }
        }

       bool has_next() const { return index < tokens.size(); }

       const std::string& peek() const
       {
        return tokens.at(index);
       }

       string consume(){
        return tokens.at(index++);
       }

       int number() {
        int num = 0;
        while (has_next() && isdigit(peek()[0])) {
            num = num * 10 + (peek()[0] - '0');
            consume();
        }
        return num;
       }

       int parse(){
        int result = 0;
        int current = number();
        string op = "+";

        while (has_next()) {
            string oper = consume();
            int next = number();
            if (oper == "+" || oper == "-") {
                result = apply(op, result, current);
                current = next;
                op = oper;
            } else {
                current = apply(oper, current, next);
            }
        }
        ans = apply(op, result, current);
        return ans;
       }
       int eval(){
           return parse();
       }

};

class Solution {
public:
    int calculate(string s) {
        Parser p(s);
        return p.eval();
    }
};