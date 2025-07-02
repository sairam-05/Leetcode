class Solution:
    def reverseWords(self, s: str) -> str:
        stack=[]
        result=''
        for i in s:
            if i!=" ":
                stack.append(i)
            else:
              while len(stack)!=0:
                result+=stack.pop()
              result+=i
              
        if len(stack)!=0:
            while len(stack)!=0:
                result+=stack.pop()
        return result
                

