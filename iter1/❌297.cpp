// BFS: a complex method...
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:
    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        string ret;
        queue<TreeNode*> q;
        q.push(root);
        queue<TreeNode*> nextq;
        while (true) {
            while (!q.empty()) {
                auto cur = q.front();
                q.pop();
                if (!cur) {
                    ret += "null,";
                } else {
                    ret += to_string(cur->val) + ",";
                    nextq.push(cur->left);
                    nextq.push(cur->right);
                }
            }
            if (nextq.empty()) break;
            q = nextq;
            nextq = queue<TreeNode*>();
        }
        ret.pop_back();
        return ret;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        int offset = 0;
        string token;
        istringstream iss(data);
        vector<TreeNode*> nodes;
        while (getline(iss, token, ',')) {
            if (token == "null") nodes.push_back(NULL);
            else nodes.push_back(new TreeNode(stoi(token)));
        }
        for (int i = 0; i < nodes.size(); ++i) {
            auto node = nodes[i];
            if (!node) {
                offset++;
                continue;
            }
            if (2*i+1-2*offset < nodes.size()) node->left = nodes[2*i+1-2*offset];
            if (2*i+2-2*offset < nodes.size()) node->right = nodes[2*i+2-2*offset];
        }
        return nodes[0];
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
//
//
//
// 
//
// preorder, a better solution
//
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        if (!root) return "#";
        return to_string(root->val) + " " + serialize(root->left) + " " + serialize(root->right);
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        istringstream iss(data);
    }

    TreeNode* _deserialize(istringstream &iss) {
        string token;
        iss >> token;
        if (token == "#") return NULL;
        auto ret = new TreeNode(stoi(token));
        ret->left = _deserialize(iss);
        ret->right = _deserialize(iss);
        return ret;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));
