class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tempSet = {}
        result = []

        for i in range(len(nums)):
            subTarget = target - nums[i]
            
            if subTarget in tempSet:
                result.append(tempSet[subTarget])
                result.append(i)
                break
            
            tempSet[nums[i]] = i

        return result