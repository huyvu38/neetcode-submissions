# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        #carry can be 0 or 1
        carry = 0
        while l1 or l2:
            x=0
            y=0
            if l1:
                x=l1.val
                l1=l1.next
            if l2:
                y=l2.val
                l2=l2.next
            total = x+y+carry
            number=total % 10
            if total >= 10:
                carry = 1
            else:
                carry = 0
            new_node = ListNode(number)
            new_node.next=None
            curr.next=new_node
            curr=curr.next
        #Last carry
        if carry == 1:
            new_node = ListNode(1)
            new_node.next=None
            curr.next=new_node
        return dummy.next
        