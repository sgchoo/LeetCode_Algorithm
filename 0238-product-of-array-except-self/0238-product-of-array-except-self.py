class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from functools import reduce

        result = []
        totalValue = reduce(lambda x, y: x*y, nums)

        for i in range(len(nums)):
            if nums[i] != 0:
                result.append(totalValue // nums[i])
            else:
                filterdList = nums[:i] + nums[i + 1:]
                filterdValue = reduce(lambda x, y: x*y, filterdList)
                result.append(filterdValue)

        return result
    