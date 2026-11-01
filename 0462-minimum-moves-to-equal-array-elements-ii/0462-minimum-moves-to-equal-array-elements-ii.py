class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        #sorting the array and calculate the middle element..
        nums.sort()
        _len = len(nums)
        mid_term = _len // 2
        mid_ele = nums[mid_term]
        
        min_moves = 0
        for i in nums:
            min_moves += abs(i - mid_ele)
        
        return min_moves
            