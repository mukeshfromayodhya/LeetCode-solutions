class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        used_index = [False] * len(nums)
        def backtrack(current):
            used = set()
            if len(nums) == len(current):
                ans.append(current[:])
                return
            for i in range(0,len(nums)):
                if used_index[i] == True:
                    continue
                if nums[i] in used:
                    continue
                else:
                    current.append(nums[i])
                    used_index[i] = True
                    used.add(nums[i])
                    backtrack(current)
                    current.pop()
                    used_index[i] = False
                    
        backtrack([])
        return ans