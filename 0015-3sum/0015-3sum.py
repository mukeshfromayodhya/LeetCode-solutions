class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        a, b, c = 0, 0, 0
        triplet = []
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            b = i + 1
            c = len(nums) - 1
            while b < c:
                total = a + nums[b] + nums[c]
                if total == 0:
                    triplet.append([a,nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
                elif total < 0:
                    b += 1
                else:
                    c -= 1
        return triplet


            
