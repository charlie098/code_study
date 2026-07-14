# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 루트에 값 없음 죽어
        if not root:
            return []
        # 덱변수 선언 (큐)
        queue = deque([root])
        # 빈 리스트 (최종 결과담는 그릇)
        result = []

        # 큐(뎈)이 있으면 
        while queue:
            # 현재 크기는 큐의 크기
            cur_size = len(queue)
            # 현재 레벨 담을 그릇
            cur_level = []

            # 현재 크기 속에서
            for i in range(cur_size):
                # 덱의 가장 왼쪽을 뽑음 (가장 처음 넣은 데이터 루트)
                curr = queue.popleft()
                # 뺀 값을 그릇에 추가
                cur_level.append(curr.val)

                # 루트값의 왼쪽가지가 있으면
                if curr.left:
                    # 큐에 왼쪽을 추가
                    queue.append(curr.left)
                # 루트값의 오른가지가 있으면
                if curr.right:
                    # 큐에 오른쪽을 추가
                    queue.append(curr.right)
            # 현재 레벨의 값들을 결과 그릇에 담음
            result.append(cur_level)

        return result