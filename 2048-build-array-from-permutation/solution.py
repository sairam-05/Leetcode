class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l=[]
        n=len(nums)
        for i in range(n):
            n=nums[nums[i]]
            l.append(n)
        return l
