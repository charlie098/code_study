# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 루트에 값 없음 두 트리 같음
        if not p and not q:
            return True

        # 덱변수 선언 (큐)
        queue1 = deque([p])
        queue2 = deque([q])
        
        # 큐 두개 있으면 
        while queue1 and queue2:
            # 트리서 가장 위에거 뽑기
            curr1 = queue1.popleft()
            curr2 = queue2.popleft()

            # 둘다 null까지 가면
            if not curr1 and not curr2:
                continue
            # 둘이 다르거나 한쪽만 null인 경우
            if not curr1 or not curr2 or curr1.val != curr2.val:
                return False
            
            # 층 아래의모든 노드 null포함 을 채워넣기
            queue1.append(curr1.left)
            queue1.append(curr1.right)

            queue2.append(curr2.left)
            queue2.append(curr2.right)

        return True        