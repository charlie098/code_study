class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #배치된 꽃밭 존재 0은 없음 1은 있음
        #추가로 몇개 추가하는 경우 이웃하지 않는가가 질문
        #n의 횟수만큼 for문 돌림
        #처음은 왼쪽부터 오른쪽으로가면서 중복하지 않는지 체크 특히 처음과 끝은 유의
        #0이 연속으로 두개 처음 또는 마지막
        #0이 연속으로 세개 중간
        #위 조건이 아닌 경우 거짓 반환
        #만약 위 조건을 찾는 경우
        #0이 둘이면 반드시 맨앞/뒤 에1을 추가
        #0이 셋이면 반드시 가운데에 1을 추가

        # 1. 양 끝에 가상의 0을 추가 (맨 앞/맨 뒤 예외 처리 제거)
        padded = [0] + flowerbed + [0]
        
        zero_count = 0
        max_flowers = 0

        for num in padded:
            if num == 0:
                zero_count += 1
            else:
                # 1을 만나면 지금까지 쌓인 0의 개수로 심을 수 있는 꽃 계산
                max_flowers += (zero_count - 1) // 2
                zero_count = 0  # 카운트 초기화

        # 마지막으로 남아있는 연속된 0들 계산
        max_flowers += (zero_count - 1) // 2

        return max_flowers >= n