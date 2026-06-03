# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #dummy is gonna be the head of new merge 2 LL
        dummy = ListNode(0)
        new_node = dummy

        while list1 and list2:
            if list1.val < list2.val:
                new_node.next = list1
                list1=list1.next
            else:
                new_node.next=list2
                list2=list2.next
            new_node=new_node.next
        if list1:
            new_node.next=list1
        if list2:
            new_node.next=list2
        return dummy.next