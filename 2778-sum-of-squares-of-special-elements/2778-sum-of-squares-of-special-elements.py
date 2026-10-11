class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            position = i + 1
            if n % position == 0:
                result += nums[i] ** 2

        return result