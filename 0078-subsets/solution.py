class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []
        def dfs(index):
            # Record the current subset (partial or complete)
            ans.append(subset.copy())
            for i in range(index, len(nums)):
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()  # Backtrack
        dfs(0)
        return ans

