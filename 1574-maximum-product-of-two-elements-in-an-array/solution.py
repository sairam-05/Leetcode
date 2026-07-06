class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            nums[i]=-nums[i]
        heapq.heapify(nums)
        l=-heapq.heappop(nums)
        s1=-heapq.heappop(nums)
        return (l-1)*(s1-1)
