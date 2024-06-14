class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        from collections import deque

        originCnt = len(nums)
        removeQue = deque(nums)
        nums.clear()

        for _ in range(originCnt):
            elem = removeQue.popleft()

            if elem != val:
                nums.append(elem)
        
        expectedNums = len(nums)

        return expectedNums
        