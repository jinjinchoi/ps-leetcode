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
    tempSet = Set.new
    nextNode = headA
    while(!nextNode.nil?)
        tempSet.add(nextNode)
        nextNode = nextNode.next
    end
    
    nextNode = headB
    while(!nextNode.nil?)
        if(tempSet.include?(nextNode))
            return nextNode
        end
        nextNode = nextNode.next
    end
    return nil
end