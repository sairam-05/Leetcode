class Solution:
    def countLargestGroup(self, n: int) -> int:
        z=Counter(sum(map(int,str(v))) for v in range(1,n+1))
        zz=Counter(z.values())
        return max(zz.items())[1]
