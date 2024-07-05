# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        i = 1
        res = []
        while curr.next: 
            i += 1
            if (prev.val < curr.val > curr.next.val) or (prev.val > curr.val < curr.next.val):
                res.append(i)
            prev = prev.next
            curr = curr.next
        if len(res) < 2:
            return [-1, -1]
        mi = float('inf')
        for i in range(len(res) - 1):
            mi = min(mi, res[i + 1] - res[i])
        return [mi, res[-1] - res[0]]
        
