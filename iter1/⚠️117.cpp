// 更好的思路：先遍历左边，然后记录左边下一层级的最右节点，接着遍历右边，左右相连
// public class Solution {
//    public void connect(TreeLinkNode root) {
//
//        while(root != null){
//            TreeLinkNode tempChild = new TreeLinkNode(0);
//            TreeLinkNode currentChild = tempChild;
//            while(root!=null){
//                if(root.left != null) { currentChild.next = root.left; currentChild = currentChild.next;}
//                if(root.right != null) { currentChild.next = root.right; currentChild = currentChild.next;}
//                root = root.next;
//            }
//            root = tempChild.next;
//        }
//    }
//}
//

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

#include <iostream>

using namespace std;

class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
            : val(_val), left(_left), right(_right), next(_next) {}
};

#include <iostream>
#include <queue>

using namespace std;

class Solution {
public:
    Node* connect(Node* root) {
        queue<pair<Node*, Node*>> q;
        q.push({root, NULL});
        while (!q.empty()) {
            auto pa = q.front(); q.pop();
            Node *cur = pa.first, *parent = pa.second;
            if (!cur) continue;
            _connect(cur, parent);
            q.push({cur->left, cur});
            q.push({cur->right, cur});
        }
        return root;
    }

    Node* _connect(Node* root, Node* parent) {
        if (!root || !parent) return root;
        else if (parent->right && parent->right != root) root->next = parent->right;
        else {
            Node* cur = parent->next;
            while (cur) {
                if (cur->left) {
                    root->next = cur->left;
                    break;
                } else if (cur->right) {
                    root->next = cur->right;
                    break;
                } else {
                    cur = cur->next;
                }
            }
        }
        return root;
    }
};

int main() {

}

