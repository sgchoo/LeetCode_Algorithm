class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        cnt1, cnt2 = Counter(s), Counter(t)

        return True if cnt1 == cnt2 else False