# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # 덱변수 선언 (큐)
        queue = deque([root])
        # 결과 배열
        result = []

        # 큐(뎈)이 있으면 
        while queue:
            # 현재 크기는 큐의 크기
            cur_size = len(queue)
            # 현재 크기 속에서
            for i in range(cur_size):
                # 덱의 가장 왼쪽 뽑음 (가장 처음 넣은 데이터 루트)
                curr = queue.popleft()

                # 가장 오른쪽 노드를 결과에 추가
                if i == cur_size - 1:
                    result.append(curr.val)

                # 루트값의 왼쪽가지가 있으면
                if curr.left:
                    # 큐에 왼쪽을 추가
                    queue.append(curr.left)
                # 루트값의 오른가지가 있으면
                if curr.right:
                    # 큐에 오른쪽을 추가
                    queue.append(curr.right)
        
        return result