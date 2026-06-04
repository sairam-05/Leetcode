class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=[]
        n=len(nums)
        freq=dict()
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        t=n//2
        for (k,v) in freq.items():
            if v>t:
                return k

