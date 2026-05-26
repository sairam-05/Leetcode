class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i in s:
            if i.isalnum():
                t+=i.lower()
        r=t[::-1]
        if t==r:
            return True
        else:
            return False
