class Solution:
    def reverseVowels(self, s: str) -> str:
        v="aeiouAEIOU"
        x=[]
        s=list(s)
        i=0
        j=len(s)-1
        while i<j:
            while i<j and s[i] not in v:
                i+=1
            while i<j and s[j] not in v:
                j-=1
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return "".join(s) 
