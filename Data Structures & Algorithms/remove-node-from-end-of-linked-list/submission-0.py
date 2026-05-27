# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# could also solve by reversing list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # facilitates removal of nth node
        dummy = ListNode(0, head)
        left = dummy

        # shifting right pointer to correct position
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # continue until right ptr reaches end of list
        while right:
            left = left.next
            right = right.next

        # left ptr at nth + 1 node from the end so can remove nth node
        left.next = left.next.next
        return dummy.next

    



