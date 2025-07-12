class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        result=[]
        n=len(nums)
        for i in range(0,n,2):
            result.append(nums[i+1])
            result.append(nums[i])
        return result
