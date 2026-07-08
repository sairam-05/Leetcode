class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res=0
        for i in num:
            res=res*10+i
        res+=k
        result=[]
        while res>0:
            d=res%10
            result.insert(0,d)
            res=res//10
        return result
