class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # 그룹 수
        provinces = 0
        # 도시 방문 여부
        visited = [False] * n

        for i in range(n):
            # 방문하지 않았다면 visited[i] 가 False라면
            if not visited[i]:
                # 그룹 추가
                provinces += 1
                # 방문 표시
                visited[i] = True
                # 큐에 i 추가
                q = deque([i])
                while q:
                    city = q.popleft()
                    # 방금 뺀 city와 연관된 도시 찾기
                    for j in range(n):
                        if isConnected[city][j] == 1 and not visited[j]:
                            visited[j] = True
                            q.append(j)
        
        return provinces