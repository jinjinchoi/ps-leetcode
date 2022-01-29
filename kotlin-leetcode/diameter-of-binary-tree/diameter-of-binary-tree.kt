/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    var max = 0
    
    fun diameterOfBinaryTree(root: TreeNode?): Int {
        maxDepthFrom(root)
        return max
    }
    
    fun maxDepthFrom(root: TreeNode?): Int{
        if(root==null) return 0
        val leftDepth = maxDepthFrom(root.left)
        val rightDepth = maxDepthFrom(root.right)
        max = maxOf(max, leftDepth+rightDepth)
        return maxOf(leftDepth, rightDepth) + 1
    }
}