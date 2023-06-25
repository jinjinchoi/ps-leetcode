# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checked_nodes = set()
        current_node = head
        while(head):
            if head in checked_nodes:
                return True
            checked_nodes.add(head)
            head = head.next
        return False