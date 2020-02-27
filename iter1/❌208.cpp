// 关键点，因为最多只有26的子节点，所以写死26个子节点既可
// 另外，对trie的概念不熟悉

#include <set>
#include <iostream>
#include <vector>

using namespace std;

class Trie {

public:
    char val = '\0';
    vector<Trie*> children = vector<Trie*>(26);
    bool isNode = false;

    /** Initialize your data structure here. */
    Trie() {}

    /** Inserts a word into the trie. */
    void insert(string word) {
        if (word.length() == 0) {
            isNode = true;
            return;
        }
        auto c = word[0];
        if (children[c-'a'] == nullptr) {
            Trie* t = new Trie();
            t->val = c;
            t->insert(word.substr(1));

            children[c-'a'] = t;
        } else {
            children[c-'a']->insert(word.substr(1));
        }
    }

    /** Returns if the word is in the trie. */
    bool search(string word) {
        if (word.length() == 0) {
            if (isNode) return true;
            else return false;
        }
        auto c = word[0];
        if (children[c-'a'] == nullptr) return false;
        return children[c-'a']->search(word.substr(1));
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        if (prefix.length() == 0) return true;
        auto c = prefix[0];
        if (children[c-'a'] == nullptr) return false;
        return children[c-'a']->startsWith(prefix.substr(1));
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */


int main() {
    Trie *t = new Trie();
    t->insert("apple");
    cout << t->search("app") << endl;
//    cout << t->search("apple") << endl;
    cout << t->startsWith("app") << endl;
}
