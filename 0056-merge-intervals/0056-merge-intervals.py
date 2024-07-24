class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        from collections import deque
        result = []
        intervals = sorted(intervals)
        que = deque(intervals)

        curDist = que.popleft()

        while True:
            if not que:
                result.append(curDist)
                break

            nextDist = que.popleft()
            curStart, curEnd = curDist[0], curDist[1]
            nextStart, nextEnd = nextDist[0], nextDist[1]
            
            if curEnd - nextStart >= 0:
                curStart = curStart if curStart < nextStart else nextStart
                nextEnd = nextEnd if nextEnd > curEnd else curEnd
                curDist = [curStart, nextEnd]
            else:       
                result.append(curDist)
                curDist = nextDist
                

        return result