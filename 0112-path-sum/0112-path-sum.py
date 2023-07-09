# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # recursive --> left 랑 right 호출하기. until leaf일 때. 
        # targetSum에서 val 빼고. 뺀 값이 0이면서 leaf이면 true
        # leaf인데 뺀 값이 0이 아니면 false. 이러면 time complexity는 node를 다 지나가니깐 ON
        
        #  DFS문제다. 
        # 
        
        if not root:
            return False
        
        stack = [(root, targetSum - root.val), ]
        while stack:
            node, curr_sum = stack.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                stack.append((node.right, curr_sum - node.right.val))
            if node.left:
                stack.append((node.left, curr_sum - node.left.val))
                
        return False