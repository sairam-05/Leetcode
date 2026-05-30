class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s=0
        m=x
        while x>0:
            n=x%10
            s+=n
            x//=10
        if m%s==0:
                return s
        else:
                return -1
