class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        if target>nums[r]:
            return r+1
        elif target<nums[l]:
            return l
        while l<=r:
            m=l+(r-l)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        if nums[m]<target:
                return m+1
        else:
            return m
        
        

        
