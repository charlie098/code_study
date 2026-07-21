# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #메인 큐
        main_queue = deque([root])

        while main_queue:
            #메인 큐에서 살펴볼 노드
            curr_node = main_queue.popleft()

            if curr_node:
                # 확인용 큐 두개
                check_q1 = deque([curr_node])
                check_q2 = deque([subRoot])
                is_same = True

                while check_q1 and check_q2:
                    #확인용 큐 노드로 재정의
                    node1 = check_q1.popleft()
                    node2 = check_q2.popleft()

                    #둘 다 없으면
                    if not node1 and not node2:
                        continue
                    #둘 중 하나만 있거나 두 노드의 값이 다르면
                    if not node1 or not node2 or node1.val != node2.val:
                        is_same = False
                        break
                    #현재 노드들의 좌,우 노드 체크 큐에 추가
                    check_q1.append(node1.left)
                    check_q1.append(node1.right)
                    check_q2.append(node2.left)
                    check_q2.append(node2.right)

                if is_same:
                    return True
                #아직 안끝났으면 메인큐에 좌,우 자식 추가 후 탐색 진행
                main_queue.append(curr_node.left)
                main_queue.append(curr_node.right)
        
        return False