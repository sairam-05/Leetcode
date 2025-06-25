class Solution:
    def secondHighest(self, s: str) -> int:
        digits=""
        for i in s:
            if i.isdigit():
                digits+=i+' '
        digi=list(map(int,digits.split()))
        max=-1
        secondlargest=-1
        for i in range(len(digi)):
            if max<digi[i]:
                secondlargest=max
                max=digi[i]
            if digi[i]>secondlargest and digi[i]!=max:
                secondlargest=digi[i]
        return secondlargest
            

                

