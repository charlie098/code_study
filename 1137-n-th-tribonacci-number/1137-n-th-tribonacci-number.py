class Solution:
    def tribonacci(self, n: int) -> int:
        # 0 1 2 일때 각각 따로 지정
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        # dp 배열 설정
        dp = [0] * (n + 1)
        # 0 1 2 에 직접 값 대입
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range (3, n+1):
            # 뒤로 세번째로 작은 수까지 합한게 i의 값
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        return dp[n]
