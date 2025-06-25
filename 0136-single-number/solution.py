class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=nums[0]
        for i in range(len(nums)-1):
            result=result^nums[i+1]
        return result
