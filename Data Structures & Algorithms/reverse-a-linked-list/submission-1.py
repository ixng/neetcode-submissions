# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next #place holder for the current node's head pointer
            curr.next = prev # sets the current head to be the previous holder
            prev = curr #sets the prev pointer to the current pointer
            curr = nxt #sets the current pointer to the next node
        
        return prev