# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(node: TreeNode, path: str):
            if not node:
                return

            # 현재 노드의 값을 경로에 추가
            path += str(node.val)

            # 1. 리프 노드에 도착했을 때: 결과 리스트에 저장하고 종료
            if not node.left and not node.right:
                result.append(path)
                return

            # 2. 자식 노드가 남아있을 때: '->'를 붙여서 아래로 계속 진행
            if node.left:
                dfs(node.left, path + "->")
            if node.right:
                dfs(node.right, path + "->")

        dfs(root, "")
        return result