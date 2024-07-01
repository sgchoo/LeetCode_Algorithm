class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # lcs = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1) ]

        # for i in range(1, len(s) + 1):
        #     for j in range(1, len(t) + 1):
        #         if s[i - 1] == t[j - 1]:
        #             lcs[i][j] = lcs[i-1][j-1] + 1
        #         else:
        #             lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
                    
        # if lcs[i][j] >= len(s) or lcs[i][j] >= len(t):
        #     return True
        # else:
        #     False

        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                
            j += 1
            
        return i == len(s)