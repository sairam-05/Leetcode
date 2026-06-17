class Solution:
    def maxDepth(self, s: str) -> int:
        c=0
        mc=0
        r=[]
        for i in s:
            if i=="(":
                c+=1
                r.append(i)
            elif i==")":
                if c>mc:
                    mc=c
                c-=1
                r.pop()
        return mc

