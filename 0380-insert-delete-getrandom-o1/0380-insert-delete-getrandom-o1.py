class RandomizedSet:
    
    def __init__(self):
        self.arr = set()
        
    def insert(self, val: int) -> bool:
        originLength = len(self.arr)
        
        self.arr.add(val)
        
        if originLength == len(self.arr):
            return False
        
        return True
        
    def remove(self, val: int) -> bool:
        originLength = len(self.arr)
        isRemoved = False
        
        self.arr.add(val)
        
        if originLength == len(self.arr):
            isRemoved = True
        
        self.arr.remove(val)
        
        return isRemoved
        
    def getRandom(self) -> int:
        if len(self.arr) == 0:
            return
        
        import random
        
        ranNum = random.randrange(len(self.arr))
        
        temp = list(self.arr)
        
        return temp[ranNum]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()