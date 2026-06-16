class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l1=[]
        p=[]
        l2=[]
        for i in nums:
            if i==pivot:
                p.append(i)
            elif i<pivot:
                l1.append(i)
            else:
                l2.append(i)
        return l1+p+l2
