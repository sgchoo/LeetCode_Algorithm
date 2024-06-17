class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # from collections import deque

        # que = deque(nums)

        # for _ in range(k):
        #     elem = que.pop()
        #     que.appendleft(elem)

        # nums.clear()
        # nums.extend(list(que))

        limit = k % len(nums)

        r = len(nums) - limit

        new = nums[0:r]
        nums[0:r] = []

        nums.extend(new)