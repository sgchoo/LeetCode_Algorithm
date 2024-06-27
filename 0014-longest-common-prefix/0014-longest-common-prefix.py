class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            prefix = ""
        else:
            prefix = strs[0]
            for i in range(1, len(strs)):
                while strs[i].find(prefix) != 0:
                    prefix = prefix[:-1]
                    if not prefix:
                        break
            

        return prefix