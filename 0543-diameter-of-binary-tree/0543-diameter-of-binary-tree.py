# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def get_depth(node):
            # 없으면 0
            if not node:
                return 0 
            
            # 왼쪽 깊이
            left_depth = get_depth(node.left)
            # 오른쪽 깊이
            right_depth = get_depth(node.right)
            
            # 좌우 깊이 구하고 최대값 갱신
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)
            
            return 1 + max(left_depth, right_depth)
        # 재귀
        get_depth(root)
        return self.max_diameter
        