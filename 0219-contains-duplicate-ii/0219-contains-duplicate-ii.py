class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_index = {}
        for i in range(0, len(nums)):
            if nums[i] not in dict_index :
                dict_index[nums[i]] = i
            elif i - dict_index[nums[i]] <= k:
                return True
            else:
                dict_index[nums[i]] = i
        
        return False