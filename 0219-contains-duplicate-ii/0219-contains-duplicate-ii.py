class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        commonList = {}

        for i in range(len(nums)):
            if nums[i] in commonList and abs(i - commonList[nums[i]]) <= k:
                return True
                
            commonList[nums[i]] = i
            
        return False