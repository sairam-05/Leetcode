class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        
        res=[]
        for r in matrix:
            s=sum(r)
            res.append(s)
        return res
