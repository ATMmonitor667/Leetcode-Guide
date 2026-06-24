class Parser
{
    private:
    vector<string>tokens{};
    size_t index{0};
    string ans = "";
    string apply(int n, string s)
    {
        string word = "";
        for(int i =0; i < n; i++) word+=s;
        return word;
    }

    public:
        Parser(const std::string& expression): index(0), ans("") 
        {
            for (char c : expression) {
                tokens.push_back(string(1, c));
            }
        }
        bool hasNext() const{
            return index < tokens.size();
        }
        const std::string& peek() const{
            return tokens.at(index);
        }
        string consume(){
            return tokens.at(index++);
        }
        int number()
        {
            int number = 0;
            while (hasNext() && isdigit(peek()[0]))
            {
                number = number * 10 + (peek()[0] - '0');
                consume();
            }
            return number;
        }
        string word()
        {
            string currWord = "";
            while(hasNext() && isalpha(peek()[0])){
                currWord = currWord + consume();
            }
            return currWord;
        }
        string parser()
        {
            string currWord = "";
            while(hasNext() && peek() != "]")
            {
                if(isdigit(peek()[0]))
                {
                    int num = number();
                    consume();
                    string inner = parser();
                    consume();
                    currWord = currWord + apply(num, inner);
                }
                else
                {
                    currWord = currWord + word();
                }
            }
            return currWord;
        }

        string decode()
        {
            ans = parser();
            return ans;
        }


};

class Solution {
public:
    string decodeString(string s) {
        Parser p(s);
        return p.decode();
    }
};