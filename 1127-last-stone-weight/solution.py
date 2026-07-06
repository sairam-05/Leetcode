
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            s1=stones.pop()
            s2=stones.pop()
            if s1!=s2:
                stones.append(abs(s1-s2))
        return stones[0] if stones else 0

