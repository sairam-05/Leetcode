class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        d={}
        for i in range(n):
            d[nums[i]]=i
        for i in range(n):
            find=target-nums[i]
            if find in d and d[find]!=i:
             return(i,d[find])
             break
