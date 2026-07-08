class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=len(nums)
        c=Counter(nums)
        gp=0
        for i,num in enumerate(nums):
            c[num]-=1
            gp+=c[num]
        return gp
