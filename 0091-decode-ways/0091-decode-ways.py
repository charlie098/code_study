class Solution:
    def numDecodings(self, s: str) -> int:
        # 규칙 0은 숫자 앞에 붙으면 안됨
        # 핵심은 2개일지 1개일지 나누는것
        # dp[i]는 s[i-1]이 0이 아니면 dp[i]는 s[i-1]이고
        # dp[i]는 s[i-2 : i]가 10~26안이면 dp[i]는 s[i-2 : i]이다
        if not s or s[0] == '0':
            return 0

        n = len(s)
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            # 한자리
            one = int(s[i - 1])
            if one != 0:
                dp[i] += dp[i - 1]
            # 두자리
            two = int(s[i-2 : i])
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
