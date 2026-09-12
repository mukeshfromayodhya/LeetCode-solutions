class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_distance = abs(target - current_sum)
                closest_distance = abs(target - closest)
                if current_distance < closest_distance:
                    closest = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum == target:
                    return current_sum
                else:
                    right -= 1
        return closest

                    