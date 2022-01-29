class Solution {
    fun invertTree(root: TreeNode?): TreeNode? {
        if(root == null) return null
        
        var treeList = LinkedList<TreeNode>()
        treeList.offer(root)
        
        while(!treeList.isEmpty()){
            val currentNode = treeList.poll()
            val temp = currentNode.left
            currentNode.left = currentNode.right
            currentNode.right = temp
            
            currentNode.left?.let{ treeList.offer(it)}
            currentNode.right?.let{treeList.offer(it)}   
        }
        
        return root
    }
}