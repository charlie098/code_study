class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # set 생성 (해시임)
        is_duple = set()

        for i in nums:
            # 해시 셋에 값이 있는가?
            if i in is_duple:
                #있다면 True 반환
                return True
            #없으면 해시셋에 값 추가
            is_duple.add(i)
        #모든 검사가 끝나면 False 반환
        return False