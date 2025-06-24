class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list=nums
        index=0
        for i in range(len(list)):
            if list[i]!=0:
                list[index]=list[i]
                index+=1
        for i in range(index,len(list)):
            list[i]=0
        
