class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = []
        tMap = []

        for i in s:
            sMap.append(s.index(i))

        for i in t:
            tMap.append(t.index(i))

        return True if sMap == tMap else False