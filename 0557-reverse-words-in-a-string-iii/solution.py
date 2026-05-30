class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        n=s.split(" ")
        for i in n:
            l.append(i[::-1])
        return " ".join(l)

