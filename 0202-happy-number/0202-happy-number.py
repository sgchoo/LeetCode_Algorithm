class Solution:
    def isHappy(self, n: int) -> bool:
        temp = str(n)
        happyNum = 0

        while True:
            if temp == '2' or temp == '4' or temp == '16':
                break
            
            for i in temp:
                happyNum += int(i)**2
                
            if happyNum == 1:
                return True

            temp = str(happyNum)
            happyNum = 0

        return False