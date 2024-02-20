import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for i in nums:
            heapq.heappush(q, -i)
        p = 0
        while k:
            p = heapq.heappop(q)
            k -= 1
        p = p * -1
        return p