class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        isDone = False
        count = 0
        pos = 0
        target = nums[0]

        while True:

            if pos > len(nums) - 1:
                    break
            
            if nums[pos] == target:
                count += 1
                if count > 2:
                    nums.remove(nums[pos])
                else:
                    pos += 1
                        
            else:
                target = nums[pos]
                count = 1
                pos += 1

        return len(nums)

    