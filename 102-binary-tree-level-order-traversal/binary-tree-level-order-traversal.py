# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = [root]
        level = []
        while q:
            l = len(q)
            p = []
            for i in range(l):
                t = q.pop(0)
                if t.left: q.append(t.left)
                if t.right: q.append(t.right)
                p.append(t.val)
            level.append(p)
        return level

