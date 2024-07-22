class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list1, list2 = [], []
        tempList = s.split(' ')

        for i in pattern:
            list1.append(pattern.find(i))
            
        for j in tempList:
            list2.append(tempList.index(j))

        return True if list1 == list2 else False