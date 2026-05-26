class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        s="".join(s)
        t="".join(t)
        if s==t:
            return True
        else:
            return False
