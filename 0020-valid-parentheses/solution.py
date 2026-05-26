class Solution:
    def isValid(self, s: str) -> bool:
       st=[]
       for i in s:
        if i=="(":
            st.append(")")
        elif i=="[":
            st.append("]")
        elif i=="{":
            st.append("}")
        elif not st or st.pop()!=i:
            return False
       return not st
            
