# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} headA
# @param {ListNode} headB
# @return {ListNode}

require 'set'

def getIntersectionNode(headA, headB)
    lengthA = 0
    lengthB = 0
    nextNode = headA
    while nextNode.next
        lengthA += 1
        nextNode = nextNode.next
    end
    nextNode = headB
    while nextNode.next
        lengthB += 1
        nextNode = nextNode.next
    end
    
    if(lengthA > lengthB)
        (lengthA-lengthB).times{headA = headA.next}
    else
        (lengthB-lengthA).times{headB = headB.next}
    end
    
    while(headA != headB)
        headA = headA.next
        headB = headB.next
    end

    return headA
end