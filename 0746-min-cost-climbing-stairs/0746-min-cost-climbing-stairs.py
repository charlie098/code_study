class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        # 계단 값 배열
        stairs = [0] * n
        # 처음 값 설정 0번에서 시작하냐 1번에서 시작하냐 차이
        stairs[0] = cost[0]
        stairs[1] = cost[1]
        # 2부터 값 측정
        for i in range(2, n):
            # 현재 계단의 값 + 이전 또는 그 전의 값은 현재 계단의 값
            stairs[i] = cost[i] + min(stairs[i-1], stairs[i-2])

        # -1번에서 가는게 값이 적은가 아님 -2에서 도착이 더 적은가
        return min(stairs[n-1], stairs[n-2])