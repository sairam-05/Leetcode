class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x=0
        for i in nums:
            if i!=val:
                nums[x]=i
                x=x+1
        return x
