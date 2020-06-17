// 优化点：用list的splice方法，可把一个节点挪到另一个地方
//

#include <vector>
#include <deque>
#include <unordered_map>
#include <list>

using namespace std;

struct MyListNode {
    int key;
    int val;
    MyListNode *prev = nullptr, *next = nullptr;
    MyListNode() {}
    MyListNode(int k, int v) : key(k), val(v) {}
};

class LRUCache {
    unordered_map<int, MyListNode*> keyToNode;
    MyListNode* root;
    int capa, cnt;

public:
    LRUCache(int capacity) {
        root = new MyListNode();
        root->next = root;
        root->prev = root;
        capa = capacity;
        cnt = 0;
    }

    int get(int key) {
        auto it = keyToNode.find(key);
        if (it == keyToNode.end()) return -1;

        auto node = it->second;
        node->prev->next = node->next;
        node->next->prev = node->prev;

        node->next = root->next;
        node->prev = root;

        root->next = node;
        node->next->prev = node;
        return node->val;
    }

    void put(int key, int value) {
        auto it = keyToNode.find(key);
        if (it != keyToNode.end()) {
            get(key);
            root->next->val = value;
            return ;
        }

        if (cnt >= capa) {
            auto node = root->prev;
            node->prev->next = node->next;
            node->next->prev = node->prev;
            keyToNode.erase(node->key);
            delete(node);
            cnt--;
        }

        auto node = new MyListNode(key, value);
        node->prev = root;
        node->next = root->next;
        node->prev->next = node;
        node->next->prev = node;

        keyToNode[node->key] = node;
        cnt++;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */

