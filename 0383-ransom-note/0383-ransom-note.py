class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        cnt1, cnt2 = Counter(ransomNote), Counter(magazine)

        if cnt1 & cnt2 == cnt1:
            return True
        return False
        # for i in magazine:
        #     for j in ransomNote:
        #         if i == j:
        #             ransomNote = ransomNote.replace(j, "", 1)
        #             print("current ransomNote is:", ransomNote)
        #             break

        # return True if len(ransomNote) == 0 else False