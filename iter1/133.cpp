//
// Created by chenyufan on 2020/4/20.
//

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;

    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }

    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }

    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Node {
public:
    int val;
    vector<Node*> neighbors;

    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }

    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }

    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
    unordered_map<int, Node*> nodes;
public:
    Node* cloneGraph(Node* node) {
        if (node == NULL) return NULL;
        _cloneGraph(node);
        return nodes[1];
    }

    void _cloneGraph(Node *node) {
        auto it = nodes.find(node->val);
        if (it != nodes.end()) return;
        auto newNode = new Node(node->val);
        nodes[node->val] = newNode;
        for (auto n : node->neighbors) {
            _cloneGraph(n);
            newNode->neighbors.push_back(nodes[n->val]);
        }
    }
};

int main() {
    Solution s;

}

