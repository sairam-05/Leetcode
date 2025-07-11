class Solution:
    mul=1
    sum=0
    result=0
    def subtractProductAndSum(self, n: int) -> int:
        while n!=0:
            self.mul*=n%10
            self.sum+=n%10
            n=n//10
 
        return self.mul-self.sum



