class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_moves = 0
        min_element = min(nums)
        for i in nums:
            min_moves += (i - min_element)
        return min_moves
