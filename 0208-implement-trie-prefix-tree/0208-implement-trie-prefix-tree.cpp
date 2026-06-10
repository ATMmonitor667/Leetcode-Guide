class Trie {
    struct TrieNode {
        unordered_map<char, TrieNode*> children;
        bool isEnd = false;
    };

    TrieNode* start;

public:
    Trie() {
        start = new TrieNode();
    }

    void insert(string word) {
        TrieNode* cursor = start;

        for(char c : word) {
            if(cursor->children.find(c) == cursor->children.end())
                cursor->children[c] = new TrieNode();

            cursor = cursor->children[c];
        }

        cursor->isEnd = true;
    }

    bool search(string word) {
        TrieNode* cursor = start;

        for(char c : word) {
            if(cursor->children.find(c) == cursor->children.end())
                return false;

            cursor = cursor->children[c];
        }

        return cursor->isEnd;
    }

    bool startsWith(string prefix) {
        TrieNode* cursor = start;

        for(char c : prefix) {
            if(cursor->children.find(c) == cursor->children.end())
                return false;

            cursor = cursor->children[c];
        }

        return true;
    }
};
/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */