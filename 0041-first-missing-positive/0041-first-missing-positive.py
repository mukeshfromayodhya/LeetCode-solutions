class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            # Positive number ho, range ke andar ho, aur correct position par na ho
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                #swap karne ke liye 
                a = nums[i] - 1
                nums[i],nums[a] = nums[a],nums[i]
        for i in range(0,len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1


            
