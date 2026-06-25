class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        l=0
        s=0
        r=len(numbers)-1
        while (l<r):
            s=numbers[l]+numbers[r]
            if  (s==target):
                res.append(l+1)
                res.append(r+1)
                break
            elif (s>target):
                r=r-1
            else:
                l=l+1
        return res
