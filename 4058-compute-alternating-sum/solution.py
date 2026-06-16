class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        s=0
        n=len(nums)
        for i in range(n):
            if i%2==0:
                s+=nums[i]
            else:
                s-=nums[i]
        return s

