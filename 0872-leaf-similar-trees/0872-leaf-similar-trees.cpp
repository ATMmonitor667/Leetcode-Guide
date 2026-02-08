/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void collect(TreeNode* root, vector<int>& result) { // <-- & here
        if (!root) return;

        if (!root->left && !root->right) {
            result.push_back(root->val);
            return;
        }
        collect(root->left, result);
        collect(root->right, result);
    }

    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> result1, result2;
        collect(root1, result1);
        collect(root2, result2);

        return result1 == result2; // simplest + safe
    }
};