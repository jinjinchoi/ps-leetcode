/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
    fun deleteNode(node: ListNode?) {
        var nextNode = node?.next
        var currentNode = node
        currentNode?.`val` = nextNode?.`val`
        currentNode?.next = nextNode?.next
    }
}