class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        # 2로 나눠서 나머지 0
        if total_sum % 2 != 0:
            return False
        # 타겟은 2로 나눈 값
        target = total_sum // 2

        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # 끝에서부터 비교 
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]

