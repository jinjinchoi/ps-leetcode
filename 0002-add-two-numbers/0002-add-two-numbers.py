# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        up = 0
        result_list = []
        l1_curr = l1
        l2_curr = l2
        answer_node = ListNode(0)
        curr = answer_node
        while l1_curr or l2_curr or up is 1:
            if not l1_curr and not l2_curr:
                digit_sum = up
            elif not l1_curr:
                digit_sum = l2_curr.val + up
                l2_curr = l2_curr.next
            elif not l2_curr:
                digit_sum = l1_curr.val + up
                l1_curr = l1_curr.next
            elif l1_curr and l2_curr:
                digit_sum = l1_curr.val + l2_curr.val + up
                l2_curr = l2_curr.next
                l1_curr = l1_curr.next
            element = digit_sum % 10
            up = digit_sum // 10
            new_node = ListNode(element)
            curr.next = new_node
            curr = new_node
        return answer_node.next
        