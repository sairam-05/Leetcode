class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n=0
        for i in nums:
            if i%3==0:
                pass
            else:
                n+=1
        return n
