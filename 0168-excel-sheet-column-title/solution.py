class Solution:
    result=""
    def convertToTitle(self, columnNumber: int) -> str:
       
        while columnNumber!=0:
            columnNumber-=1
            self.char=chr(columnNumber%26+65)
            self.result=self.char+self.result
            columnNumber=columnNumber//26
        return self.result
