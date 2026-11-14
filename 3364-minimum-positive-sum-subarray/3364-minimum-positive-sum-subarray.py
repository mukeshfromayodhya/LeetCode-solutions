class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                length = j - i + 1

                if l <= length <= r and current_sum > 0:
                    min_sum = min(min_sum,current_sum)

        return min_sum if min_sum != float('inf') else -1