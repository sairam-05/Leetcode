class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       maximum=0
       windowsum=0
       n=len(nums)
       for i in range(0,k):
        windowsum+=nums[i]
       maximum=windowsum
       for i in range(k,n):
        windowsum=windowsum+nums[i]-nums[i-k]
        maximum=max(windowsum,maximum)
       return (maximum/k)
