class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root == NULL) return root;

        //swapping left and right child
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;

        invertTree(root->left);
        invertTree(root->right);

        return root;
    }
};