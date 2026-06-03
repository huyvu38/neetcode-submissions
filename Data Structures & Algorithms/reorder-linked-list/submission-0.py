# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        #make sure current and next node not null
        while fast and fast.next:
            slow= slow.next
            fast=fast.next.next
        #after this slow point to middle
        #Reverse second half
        prev = None
        curr= slow.next
        slow.next = None
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        #Merge again
        first, second = head, prev
        while second:
            tmp1 =first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2
