class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        left = 0
        right = m
        while left <= right:
            i = (left + right)//2
            j = ((m + n+ 1) // 2) - i
            if i == 0:
                nums1_left = float("-inf")
            else:
                nums1_left = nums1[i - 1]
            
            if i == m:
                nums1_right = float("+inf")
            else:
                nums1_right = nums1[i]
            
            if j == 0:
                nums2_left = float("-inf")
            else:
                nums2_left = nums2[j - 1]
            
            if j == n:
                nums2_right = float("+inf")
            else:
                nums2_right = nums2[j]
# to check implement main logic
            
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m+n) % 2 != 0:
                    median = max(nums1_left, nums2_left)
                else:
                    left_max  = max(nums1_left, nums2_left)
                    right_min = min(nums1_right, nums2_right)
                    median = (left_max + right_min) / 2
                return median
            elif nums1_left > nums2_right:
                right = i -1
            else:
                left = i +1
            
                