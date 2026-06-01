class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_l=list(ransomNote)
        m_l=list(magazine)
        r=[]
        for i in r_l:
            if i in m_l:
                m_l.remove(i)
                r.append(i)
        if len(r)==len(r_l):
            return True
        else:
            return False
