# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        c=1
        ptr=head
        while ptr.next!=None:
            c+=1
            ptr=ptr.next
        ptr.next=head
        k=k%c
        for i in range(c-k):
            ptr=ptr.next
        res=ptr.next
        ptr.next=None
        return res
