class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            int_i = 27 - (ord(s[i])- 96)
            product = (i + 1) * int_i
            total += product
        return total