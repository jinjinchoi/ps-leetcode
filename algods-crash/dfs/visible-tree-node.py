def visible_tree_node(root) -> int:
    def dfs(root, max_till_now):
        if not root:
            return 0

        total = 0
        if root.val > max_till_now:
            total += 1

        total += dfs(root.left, max(root.val, max_till_now))
        total += dfs(root.right, max(root.val, max_till_now))
        return total


    return dfs(root, -float('inf'))
