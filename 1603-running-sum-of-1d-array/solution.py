from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=accumulate(nums)
        return list(a)
