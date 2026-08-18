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

        zero_count = 0
        max_flowers = 0
        has_one = False  # 배열에 1이 한 번이라도 나왔는지 여부

        for num in flowerbed:
            if num == 0:
                zero_count += 1
            else:
                if not has_one:
                    # [맨 앞] 첫 1을 만나기 전: 0이 2개당 꽃 1개 (zero_count // 2)
                    max_flowers += zero_count // 2
                    has_one = True
                else:
                    # [중간] 1과 1 사이: 0이 3개당 꽃 1개 ((zero_count - 1) // 2)
                    max_flowers += (zero_count - 1) // 2
                zero_count = 0  # 카운터 리셋

        # 루프가 끝나고 남은 끝부분 0 처리
        if not has_one:
            # [특수 케이스] 배열 전체가 0일 때: (zero_count + 1) // 2
            max_flowers += (zero_count + 1) // 2
        else:
            # [맨 뒤] 마지막 1 이후: 0이 2개당 꽃 1개 (zero_count // 2)
            max_flowers += zero_count // 2

        return max_flowers >= n