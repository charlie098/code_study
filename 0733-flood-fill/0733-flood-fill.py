class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]

        # 시작지점이 입력값과 같은 곳이면
        if start_color == color:
            # 값 리턴
            return image
        
        rows, cols = len(image), len(image[0])
        queue = deque([(sr, sc)])
        image[sr][sc] = color

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while queue:
            y, x = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= ny < rows and 0 <= nx < cols:
                    if image[ny][nx] == start_color:
                        image[ny][nx] = color
                        queue.append((ny, nx))

        return image