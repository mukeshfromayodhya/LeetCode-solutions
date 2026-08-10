class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # first occurences
        left = 0
        right = len(nums) -1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid +1
        
        #second occurences
        left = 0
        right = len(nums) -1
        last = -1
        while left<=right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid
                left = mid +1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1

        return [first,last]


