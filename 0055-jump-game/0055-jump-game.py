class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        # 갈 수 있는 최대 위치 (1번째 칸 = 1)
        jumpLen = 1  

        for i, num in enumerate(nums):
            # 1. 현재 발판(i + 1번째 칸)이
            # 최대 위치보다 멀다면 실패
            if (i + 1) > jumpLen:
                return False
            
            # 2. 현재 발판에서 갈 수 있는 거리(현재 위치 + num)와
            # 기존 jumpLen 중 더 큰 값으로 갱신
            jumpLen = max(jumpLen, (i + 1) + num)
            
            # 3. 도달 가능 거리가 이미 배열 길이 이상이면 성공!
            if jumpLen >= length:
                return True
                
        return True

                

