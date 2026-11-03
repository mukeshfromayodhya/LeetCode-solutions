class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = max(nums)
        count = 0
        for i in nums:
            if i < target :
                count = count + (target - i)
            
                
        return count