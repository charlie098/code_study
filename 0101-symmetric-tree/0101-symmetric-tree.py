# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        
        def isMirror(p, q):
            # 둘 다 null이면 대칭
            if not p and not q:
                return True
            # 한쪽만 null이거나 값이 다르면 대칭이 아님
            if not p or not q or p.val != q.val:
                return False
            
            # p의 왼쪽 vs q의 오른쪽, p의 오른쪽 vs q의 왼쪽을 교차해서 비교
            return isMirror(p.left, q.right) and isMirror(p.right, q.left)
            
        # 루트의 왼쪽 자식과 오른쪽 자식을 비교 시작
        return isMirror(root.left, root.right)