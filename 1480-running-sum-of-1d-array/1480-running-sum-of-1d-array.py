class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total_sum = 0
        sum_list = []
        for i in range(0, len(nums)):
            total_sum += nums[i]
            sum_list.append(total_sum)
        return sum_list
