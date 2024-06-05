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
    TreeNode* prev = nullptr;
    int minDif=INT_MAX;
    int getMinimumDifference(TreeNode* root) {
         inOrderT(root);
         return minDif;
    }
    void inOrderT(TreeNode* root){
        if(root==nullptr){
            return;
        }
        inOrderT(root->left);
        if(prev!=nullptr){
            minDif=min(minDif, abs(root->val - prev->val));
        }
        prev = root;
        inOrderT(root->right);
    }
};