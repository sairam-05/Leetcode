class Solution:
    sum=0
    digit=0
    def differenceOfSum(self, nums: List[int]) -> int:
        for i in nums:
            self.sum+=i
            while i>0:
                self.digit+=i%10
                i=i//10
        return self.sum-self.digit 
