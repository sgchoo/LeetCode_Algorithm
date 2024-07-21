class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in magazine:
            for j in ransomNote:
                if i == j:
                    ransomNote = ransomNote.replace(j, "", 1)
                    print("current ransomNote is:", ransomNote)
                    break

        return True if len(ransomNote) == 0 else False