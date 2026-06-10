class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d={}
        l=nums
        for  i in range(len(nums)):
            if l[i] in d:
                return l[i]
            else:
                d[l[i]]=1
            
