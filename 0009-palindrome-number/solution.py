class Solution:
    def isPalindrome(self, x: int) -> bool:
     num=str(x)
   
     num=num[::-1]
 
     if num==str(x):
        return True
     else:
        return False
