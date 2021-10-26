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
    fun invertTree(root: TreeNode?): TreeNode? {
        if(root == null) return null
        val leftNode: TreeNode? = root.left
        val rightNode: TreeNode? = root.right
        root.left = invertTree(rightNode)
        root.right = invertTree(leftNode)
        return root
    }
}