class Solution {
    int dia = 0 ;
    public int diameterOfBinaryTree(TreeNode root) {
        maxheight(root) ;
        return dia ;
    }
    private int maxheight(TreeNode root) {
        if (root == null) 
            return 0;
    
        int left = maxheight(root.left);
        int right = maxheight(root.right);    
        dia = Math.max(dia , left + right) ;
        
        return Math.max(left, right) + 1;
    }
}
