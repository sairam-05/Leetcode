class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d={}
        r=0
        for  i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for k,v in d.items():
            if v<2:
                r+=k
        if r>0:
            return r
        else:
            return 0

