class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                x = str(nums[j]) + str(nums[j + 1])
                y = str(nums[j + 1]) + str(nums[j])

                if x < y:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        result = ''.join(map(str, nums))

        if result[0] == "0":
            return "0"

        return result