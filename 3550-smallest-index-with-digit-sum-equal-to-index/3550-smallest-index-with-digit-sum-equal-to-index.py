class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(n):
            total = 0
            while n>0:
                total += n % 10
                n //= 10
            return total 
        
        for i, num in enumerate(nums):
            if i == digit_sum(num):
                return i
        return -1
                

