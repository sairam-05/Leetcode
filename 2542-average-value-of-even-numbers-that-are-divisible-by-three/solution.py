class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count=0
        sum1=0
        for i in nums:
            if i%2==0 and i%3==0:
                sum1+=i
                count+=1
        if sum1!=0:
            return sum1//count
        else:
            return sum1
