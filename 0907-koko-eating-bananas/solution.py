import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        def t_sum(mid):
            d=0
            for i in range(len(piles)):
                s=math.ceil(piles[i]/mid)
                d+=s
            return d
        while low<=high:
            mid=(low+high)//2
            hours=t_sum(mid)
            if hours<=h:
                high=mid-1
            else:
                low=mid+1
        return low
