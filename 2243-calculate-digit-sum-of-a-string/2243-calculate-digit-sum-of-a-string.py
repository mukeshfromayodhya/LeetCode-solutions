class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k :
            str_sum = ""
            for i in range(0,len(s), k):
                # this is use slicing for adding group chars
                sum_group = sum(int(digit) for digit in s[i:i +k]) 
                # store group's sum in str
                str_sum += str(sum_group)
            s = str_sum
        return s

            


