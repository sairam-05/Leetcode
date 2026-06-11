class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        r=x
        while (l<=r):
            m=(l+r)//2
            msq=m*m
            if msq==x:
                return m
            elif msq<x:
                l=m+1
            else:
                r=m-1
        return r
