class Solution {
    fun countNodes(root: TreeNode?): Int {
        if(root==null) return 0
        val height = calculateHeight(root)
        val rightHight = calculateHeight(root.right)
        if (rightHight == (height - 1) ) return (1 shl height-1) + countNodes(root.right) 
        else return (1 shl height-2) + countNodes(root.left)
    }
    
    fun calculateHeight(root: TreeNode?): Int{
        return if (root==null)  0 else 1 + calculateHeight(root.left)
    }
}