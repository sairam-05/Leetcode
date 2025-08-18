class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        s1=set()
        for i in range(1,n+1):
            s1.add(i)
        return list(s1.difference(set(nums)))
