class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        t=(n+1)//2
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for k,v in freq.items():
            if v>=t:
                return k
        
