class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #반복문의 경우는 이전 결과를 붙여가며 측정
        #백트래킹의 경우 아래 재귀 함수를 사용해 풀이함

        result = []

        def backtrack(start: int, path: List[int]):
            # 1. 현재 완성된 부분집합을 결과에 추가 (복사본 [:] 저장)
            result.append(path[:])

            # 2. 현재 인덱스(start)부터 끝까지 원소를 하나씩 탐색
            for i in range(start, len(nums)):
                # [가지 늘리기] 원소 선택
                path.append(nums[i])

                # [다음 단계] 다음 인덱스로 들어가 재귀 호출
                backtrack(i + 1, path)

                # [가지 치기/돌아오기] 원소 제거 (원상복구)
                path.pop()

        # index 0, 빈 리스트 [] 부터 시작
        backtrack(0, [])
        return result