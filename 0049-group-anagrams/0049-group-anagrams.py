class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import copy

        tempStrs = copy.deepcopy(strs)
        anagramsList = []
        anagramsDict = {}
        count = 0

        for i in range(len(tempStrs)):
            tempStrs[i] = sorted(tempStrs[i])
            string = ''.join(tempStrs[i])
            if string not in anagramsDict:
                anagramsDict[string] = count
                anagramsList.append([strs[i]])
                count += 1
            else:
                anagramsList[anagramsDict[string]] = anagramsList[anagramsDict[string]] + [strs[i]]
                
        return anagramsList