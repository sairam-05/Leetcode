class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n=0
        m=0
        for i in s:
            n+=ord(i)
        for i in t:
            m+=ord(i)
        return chr(m-n)
