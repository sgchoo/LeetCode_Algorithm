class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = nums[0]

        for i in range(1, len(nums)):
            if start == 0:
                return False

            start -= 1

            start = max(start, nums[i])

        return True

        # def DFS(start: int, arr: list) -> bool:
        #     if start >= len(arr) - 1:
        #         return True
        #     if nums[start] == 0:
        #         return False

        #     for i in range(1, arr[start] + 1):
        #         if DFS(start + i, arr):
        #             return True

        #     return False

        # reach = DFS(0, nums)

        # return reach