# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]
        l2=[]
        ptr=head
        pos=1
        while ptr:
            if pos%2==0:
                l1.append(ptr.val)
            else:
                l2.append(ptr.val)
            ptr=ptr.next
            pos+=1
        l3=l2+l1
        cur=head
        i=0
        while cur:
            cur.val=l3[i]
            i+=1
            cur=cur.next
        return head

