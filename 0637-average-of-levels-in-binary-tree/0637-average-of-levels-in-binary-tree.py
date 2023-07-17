from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        tree_dict = defaultdict(list)
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop()
            tree_dict[level].append(node.val)
            if node.left is not None:
                queue.append((node.left,level+1))
            if node.right is not None:
                queue.append((node.right, level+1))
        return [sum(tree_dict[i])/len(tree_dict[i]) for i in range(len(tree_dict))]
            