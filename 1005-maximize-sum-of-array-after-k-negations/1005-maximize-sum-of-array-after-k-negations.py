class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        #양수는 짝수번 음수는 홀수번 할당해야 합이 제일 커짐
        #뒤집는 수 k는 정해짐 따라서 가장 음수가 가장 작게 나와야 됨
        #그리고 그 합을 구해야 함

        # 1. 작은 수(가장 큰 음수)부터 앞으로 오도록 정렬
        nums.sort()
        
        # 2. 음수들을 절댓값이 큰 순서대로 양수로 전환
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
        
        # 3. 남은 k가 홀수라면, 가장 작은 수 1개만 음수로 전환
        # (이미 2단계에서 양수로 다 바뀌었으므로 다시 정렬 후 가장 작은 값 변경)
        if k % 2 == 1:
            nums.sort()
            nums[0] = -nums[0]
            
        return sum(nums)