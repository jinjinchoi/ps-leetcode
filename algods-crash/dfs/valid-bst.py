def valid_bst(root):
    def dfs(root, min_range, max_range):
        if not root:
            return True
        if not (min_range <= root.val <= max_range):
            return False
        return dfs(root.left, min_range, root.val) and dfs(root.right, root.val, max_range)
    
    return dfs(root, -float('inf'), float('inf'))

