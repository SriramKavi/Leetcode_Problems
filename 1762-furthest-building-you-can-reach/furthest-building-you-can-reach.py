import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(q, -diff)
                bricks -= diff
                if bricks < 0 and ladders > 0:
                    bricks += -heapq.heappop(q)
                    ladders -= 1
            if ladders <= 0 and bricks < 0:
                return i
        return len(heights) - 1
