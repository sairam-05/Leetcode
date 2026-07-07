class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l1=sentence.split()
        l=len(searchWord)
        for i in range(len(l1)):
            name1=str(l1[i])
            if len(l1[i])>=len(searchWord) and name1[:l]==searchWord:
                return i+1
        return -1
