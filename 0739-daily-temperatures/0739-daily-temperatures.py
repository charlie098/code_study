class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 너무 오래 걸리니 리스트를 쓰자
        res = [0] * len(temperatures)
        temp = []
        #i는 인덱스 data는 temperature의 i해당값
        for i, data in enumerate(temperatures):
            # 최신값과 비교
            while temp and data > temperatures[temp[-1]]:
                # 있으면 빼기
                latest = temp.pop()
                # 뺀 값 배열에 추가
                res[latest] = i - latest            
            temp.append(i)
        return res





        # 비교대상이 자신보다 크면 1증가 후 리턴
        # 비교대상이 자기보다 작으면 1증가
        # for문 두번은 너무 오래걸림
        # result = []
        # lastIdx = len(temperatures)
        # for i, temp in enumerate(temperatures):
        #     count = 0
        #     if i == lastIdx - 1:
        #         result.append(count)
        #         return result
        #     for j in range(i, lastIdx):
        #         if j + 1 == lastIdx:
        #             result.append(0)
        #             break
        #         if temp < temperatures[j+1]:
        #             count = count + 1
        #             result.append(count)
        #             break
        #         else:
        #             count = count + 1
