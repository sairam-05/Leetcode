class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d={}
        for k,v in enumerate(sorted(nums)):
            if v not in d:
                d[v]=k
        ans=[d[v] for v in nums]
        return ans
