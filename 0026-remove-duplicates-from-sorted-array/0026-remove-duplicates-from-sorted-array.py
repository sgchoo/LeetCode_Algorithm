class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import deque

        originCnt = len(nums)
        que = deque(nums)
        nums.clear()

        nums.append(que.popleft())
        # under the assumption that it is sorted
        for _ in range(originCnt - 1):
            elem = que.popleft()
            if nums[-1] != elem:
                nums.append(elem)

        return len(nums)