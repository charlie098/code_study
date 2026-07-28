class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #1원부터 목표까지 리스트의 값으로 가장 적은 수를 카운트
        #이 때 가장 중요한 것은 위 값들을 리스트(값)로 저장
        #그 후 큰 값을 구할 때 리스트(값)에서 결과를 불러와서 계산
        #예를 들면 4면 3을 구할때랑 1을 구할때를 더하거나, 2를 구할때를 두번

        # 배열 초기화(최대값으로 0을 제외한 나머지 채우기)
        results = [amount + 1] * (amount + 1)
        # 0개를 만드는 수는 0
        results[0] = 0
        
        # 만들 수 있는 값 검사(1원부터 목표값까지)
        for i in range (1, amount + 1):
            for coin in coins:
                
                #동전의 값은 i와 같거나 작아야 됨(그래야 잔돈 또는 딱맞기 때문)
                if i - coin >= 0:
                    #기존 값 results[i]와 results[i - coin] + 1 개 중 누가 더 작은지 비교
                    results[i] = min(results[i], results[i - coin] + 1)
        
        # 목표 금액을 맟추는 대 들어가는 코인 수가 돈의 값보다 큰 경우는 -1 리턴
        if results[amount] > amount:
            return -1 


        return results[amount]
