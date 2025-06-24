class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        list=nums
        index=1
        for i in range(1,len(list)):
            if list[i-1]!=list[i]:
                list[index]=list[i]
                index+=1
        return index
