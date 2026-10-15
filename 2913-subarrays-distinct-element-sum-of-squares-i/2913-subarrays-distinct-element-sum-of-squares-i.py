class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(n):
            distinct = set()
            for j in range(i,n):
                distinct.add(nums[j])
                total += len(distinct) ** 2
        return total