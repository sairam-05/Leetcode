class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            l=0
            h=len(nums)-1
            while l<=h:
                m=(l+h)//2
                if nums[m]<x:
                    l=m+1
                else:
                    h=m-1
            return l
        l=search(target)
        h=search(target+1)-1
        if l<=h:
            return [l,h]
        else:
            return [-1,-1]
