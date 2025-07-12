class Solution:
    count=0
    def countDigits(self, num: int) -> int:
        count=0
        for i in str(num):
            d = int(i)
            if d != 0 and num % d == 0:
                count += 1
        return count
