class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            # Find the minimum value and its first index
            min_val = min(nums)
            idx = nums.index(min_val)
            nums[idx] = min_val * multiplier
        return nums
