# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        ptr=head
        while ptr:
            l.append(ptr.val)
            ptr=ptr.next
        if l==l[::-1]:
            return True
        else:
            return False

