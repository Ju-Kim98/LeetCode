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
private:
    bool set[1001] = {};
    void dfs(TreeNode* &root, bool flag, vector<TreeNode*>& result){
        if (root == nullptr) 
            return;
        dfs(root->left, set[root->val], result);
        dfs(root->right, set[root->val], result);
        if (!set[root->val] && flag) result.push_back(root);
        if(set[root->val]) root = nullptr;
    }
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        vector<TreeNode*> result;
        for(int num : to_delete)
            set[num] = true;
        dfs(root, true, result);
        return result;
    }
};