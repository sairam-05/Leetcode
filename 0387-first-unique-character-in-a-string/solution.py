from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
        for i,k in enumerate(s):
            if count[k]==1:
                return i
        return -1

