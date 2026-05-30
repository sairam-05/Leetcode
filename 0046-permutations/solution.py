from itertools import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=permutations(nums)
        return list(n)
