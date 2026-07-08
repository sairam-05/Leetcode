class Solution:
    def sumBase(self, n: int,k: int) -> int:
        s=0
        while n>0:
            d=n%k
            s+=d
            n=n//k
        return s
