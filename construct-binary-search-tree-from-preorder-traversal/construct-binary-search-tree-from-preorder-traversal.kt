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
    fun bstFromPreorder(preorder: IntArray): TreeNode? {
        val root = TreeNode(preorder[0])
        preorder.forEach{ value -> 
            bfs(root, value)
        }
        return root
    }
    
    fun bfs(root: TreeNode, num: Int){
        if(root.`val` == num) return
        if(root.`val` > num) root.left?.let{ 
            bfs(it, num)
        } ?: run{ 
            root.left = TreeNode(num)
        }else root.right?.let{ 
            bfs(it, num)
        } ?: run{ 
            root.right = TreeNode(num)
        }
    }
}