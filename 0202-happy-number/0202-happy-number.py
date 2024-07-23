class Solution:
    def isHappy(self, n: int) -> bool:
        temp = str(n)
        happyNum = 0
        resultList = []

        while True:
            if temp in resultList:
                break
            
            for i in temp:
                happyNum += int(i)**2
                
            if happyNum == 1:
                return True

            resultList.append(temp)
            temp = str(happyNum)
            happyNum = 0

        return False