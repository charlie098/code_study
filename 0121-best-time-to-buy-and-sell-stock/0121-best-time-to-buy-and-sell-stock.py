class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 싼가격 체크
        # 최대 이익 체크
        # 지금까지의 최저가를 저장할 변수 (처음엔 아주 큰 값으로 초기화)
        min_price = float('inf')
        # 최대 이익을 저장할 변수
        max_profit = 0

        for price in prices:
            # 1. 지금까지 등장한 가장 싼 주가 갱신
            if price < min_price:
                min_price = price
            # 2. 오늘 팔았을 때의 이익(오늘 가격 - 최저가)이 기존 최대 이익보다 크면 갱신
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit