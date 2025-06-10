class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
        else:
            sign=1
        if sign==-1:
            x=-x
        num=str(x)[::-1]
        num=int(num)
        if num  not in range(-2**31,(2**31)-1):
            return 0

        return num*sign
