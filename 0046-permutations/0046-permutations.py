class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        def backtrack(current):
            if len(current) == len(nums):
                ans.append(current[:])
                
            for i in range(0, len(nums)):
                if nums[i] in current:
                    continue
                else:
                    current.append(nums[i])
                    backtrack(current)
                    current.pop()
        backtrack([])
        return ans  
                    
                
       
