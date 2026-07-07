class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        a="a"
        words=sentence.split()
        for i in range(len(words)):
            if words[i][0] in "aeiouAEIOU":
                words[i]+="ma"
            else:
                words[i]=words[i][1:]+words[i][0]+"ma"
            words[i]+=a
            a+="a"
        return " ".join(words)
