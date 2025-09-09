class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x:int)->int:
            low=0
            high=len(nums)-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]<x:
                    low=mid+1
                else:
                    high=mid-1
            return low
        l=search(target)
        h=search(target+1)-1
        if l<=h:
            return [l,h]
        else:
            return[-1,-1]
