class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        from collections import deque

        numQue = deque(nums)
        result = []
        que = deque()

        for i in range(len(nums)):
            elem = numQue.popleft()

            if elem + 2 == 2:
                que.appendleft(elem)
            elif elem + 1 == 2:
                que.append(elem)
            else:
                numQue.append(elem)
        
        result = list(que)

        result = result + list(numQue)

        nums.clear()
        nums.extend(result)