class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count_increase = 1
        count_decrease = 1
        max_length = 1

        for i in range(len(nums) - 1):

            if nums[i] < nums[i + 1]:
                count_increase += 1
                count_decrease = 1

            elif nums[i] > nums[i + 1]:
                count_decrease += 1
                count_increase = 1

            else:
                count_increase = 1
                count_decrease = 1

            max_length = max(max_length, count_increase, count_decrease)

        return max_length