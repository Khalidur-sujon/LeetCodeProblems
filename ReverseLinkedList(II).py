# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)

        # reach at left node
        leftprev, curr = dummyNode, head
        for i in range(left - 1):
            leftprev, curr = curr, curr.next
        
        # left to right
        # reverse
        prev = None
        for i in range(right - left + 1):
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp

        # connect all nodes
        leftprev.next.next = curr
        leftprev.next = prev
        
        return dummyNode.next
