# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return - 1
        q = [root]
        li = []
        while q:
            s = 0
            l = len(q)
            for i in range(l):
                p = q.pop(0)
                if p.left: q.append(p.left)
                if p.right: q.append(p.right)
                s += p.val
            li.append(s)
        if len(li) == 0: return -1
        if k > len(li): return -1
        print(li)
        li.sort()
        return li[-k]