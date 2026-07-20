class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        
        min = 0
        # 방향
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue and fresh > 0:
            min += 1
            for _ in range(len(queue)):
                #썩은 오랜지 좌표 꺼내기
                i, j = queue.popleft()
                
                for di, dj in dirs:
                    #썩은 오랜지 좌표에 방향 더한값(썩혀야 되는 좌표)
                    ni, nj = i + di, j + dj
                    #썩혀야 되는 좌표에 멀쩡한 오랜지가 있는 경우
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        #썩은 것으로 교체
                        grid[ni][nj] = 2
                        fresh -= 1
                        #썩은 것 좌표 추가
                        queue.append((ni, nj))

        #신선한 오랜지가 사라지면 리턴 또는 하나라도 남으면 -1
        return min if fresh == 0 else -1
