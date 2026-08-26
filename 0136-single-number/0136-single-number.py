class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single_num = 0
        for i in range(0,len(nums)):
            single_num = single_num ^ nums[i] 
        return single_num