class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, curSum = 0, 0, nums[0]
        res = int(1e9)

        while True:
            if curSum >= target:
                res = min(res, right - left + 1)
                curSum -= nums[left]
                left += 1
            else:
                right += 1
                if right >= len(nums):
                    break
                curSum += nums[right]
                
        return res if res != int(1e9) else 0