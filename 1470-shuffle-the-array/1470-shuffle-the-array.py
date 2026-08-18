class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final_nums = []
        nums1 = []
        nums2 = []
        for n1 in range(0,len(nums)//2):
            nums1.append(nums[n1])
        for n2 in range(len(nums)//2, len(nums)):
            nums2.append(nums[n2])
        for i in range(0,n):
            final_nums.append(nums1[i])
            final_nums.append(nums2[i])
        
        return final_nums
