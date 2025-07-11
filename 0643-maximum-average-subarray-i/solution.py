class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=0
        n=len(nums)
        for i in range(k):
            s+=nums[i]
        maximum=s
        for i in range(k,n):
            s=s+nums[i]-nums[i-k]
            maximum=max(maximum,s)
        return maximum/k
