class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        return True if str(x) == str(x)[::-1] else False