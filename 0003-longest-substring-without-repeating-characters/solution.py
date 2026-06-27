class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1=set()
        l=0
       
        lon=0
        n=len(s)
        for r in range(n):
            while s[r] in s1:
                s1.remove(s[l])
                l+=1
            w=(r-l)+1
            lon=max(w,lon)
            s1.add(s[r])
        return lon


