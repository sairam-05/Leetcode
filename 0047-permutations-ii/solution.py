from itertools import *
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=permutations(nums)
        return list(set(n))
