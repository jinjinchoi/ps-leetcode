class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
def middle_of_linked_list(head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next
    return slow

inputs = ["0 1 2 3 4","0 1 2 3 4 5"]
for i in range(len(inputs)):
    dummy = ListNode(-1)
    cur = dummy
    for val in inputs[i].split():
        node = ListNode(int(val))
        cur.next = node
        cur = node
    res = middle_of_linked_list(dummy.next)

    if not res:
        actual_output = None
    else:
        actual_output = res.val
    print("Middle of linked list :",actual_output)
