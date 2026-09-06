class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        index = 0
        current_subset = []
        answer = []
        def backtrack(index,current_subset):
            if index == len(nums):
                answer.append(current_subset[:])
            else:
                current_subset.append(nums[index])
                backtrack(index +1, current_subset)
                current_subset.pop()
                backtrack(index + 1, current_subset)
        backtrack(index,current_subset)
        return answer



