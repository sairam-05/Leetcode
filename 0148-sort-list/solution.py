# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        ptr=head
        c=ListNode()
        while ptr:
            l.append(ptr.val)
            ptr=ptr.next
        l.sort()
        curr=head
        i=0
        while curr:
            curr.val=l[i]
            i+=1
            curr=curr.next
        return head
