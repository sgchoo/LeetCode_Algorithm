class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import math

        nums = sorted(nums)

        target = nums[0]
        majorityElement = math.ceil(len(nums) / 2)
        count = 0

        for i in range(len(nums)):
            if count >= majorityElement:
                break
            
            if target == nums[i]:
                count += 1
            else:
                target = nums[i]
                count = 1
        
        return target

