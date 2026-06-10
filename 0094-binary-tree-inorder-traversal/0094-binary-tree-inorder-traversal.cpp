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
    vector<int> inorderTraversal(TreeNode* root) {

        vector<int> result;

        auto dfs = [&](auto&& dfs, TreeNode* root, vector<int>& result) -> void {
            if (root == nullptr) {
                return;
            }

            dfs(dfs, root->left, result);
            result.push_back(root->val);
            dfs(dfs, root->right, result);
        };

        dfs(dfs, root, result);
        return result;
    }
};