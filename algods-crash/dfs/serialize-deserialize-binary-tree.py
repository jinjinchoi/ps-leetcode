def serialize(root):
      string_array = []
      def dfs(root):
            if not root:
                  string_array.append('x')
                  return
            string_array.append(root.val)
            dfs(root.left)
            dfs(root.right)
      dfs(root)
      return ' '.join(str(string) for string in string_array)

def deserialize(s):
      def dfs(nodes):
            val = next(nodes)
            if val == 'x': return
            curr = Node(int(val))
            curr.left = dfs(nodes)
            curr.right = dfs(nodes)
            return curr
      return dfs(iter(s.split()))
