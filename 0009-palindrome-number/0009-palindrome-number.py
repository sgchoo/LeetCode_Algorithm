class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # return True if str(x) == str(x)[::-1] else False
        origin = x
        reverse = 0

        while x > 0:
            reverse = reverse * 10 + x % 10
            x = x // 10

        return True if origin == reverse else False