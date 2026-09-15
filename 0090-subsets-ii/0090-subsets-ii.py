class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        start = 0
        current = []
        ans = []
        def backtrack(start, current):
            ans.append(current[:])
            for i in range (start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                else:
                    current.append(nums[i])
                    backtrack(i + 1, current)
                    current.pop()
        backtrack(start, current)
        return ans




