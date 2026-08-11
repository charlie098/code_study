class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 가장 작은 점수 애들 1개
        # 1개 옆의 애들 점수가 높으면? +1
        # 양 옆의 아이와 점수가 같은 경우? 사탕 수는 1로 초기화

        n = len(ratings)
        if n == 0:
            return 0
        
        total = 1   # 첫 번째 아이 기본 사탕 1개
        up = 0      # 오르막길 길이
        down = 0    # 내리막길 길이
        peak = 0    # 가장 높았던 산봉우리 높이
        
        for i in range(1, n):
            # 1. 오르막길
            if ratings[i] > ratings[i - 1]:
                up += 1
                down = 0
                peak = up
                total += (1 + up)  # 기본 1개 + 오르막 누적값 더함
                
            # 2. 평지 (점수 같음)
            elif ratings[i] == ratings[i - 1]:
                up = 0
                down = 0
                peak = 0
                total += 1  # 점수 같으면 1개만 더함
                
            # 3. 내리막길
            else:
                up = 0
                down += 1
                # 1. 내리막길에 포함된 아이들 수(down)만큼 먼저 사탕을 누적
                total += down
                # 2. 내리막길이 산봉우리 높이(peak)를 넘어서면, 산봉우리 아이도 1개 더 받아야 하므로 +1
                if down > peak:
                    total += 1
                
        return total           



                