class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        moscode=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result=[]
        for i in words:
            str1=""
            for ch in i:
                str1+=moscode[ord(ch)-97]
            result.append(str1)
        s=set(result)
        return len(s)
