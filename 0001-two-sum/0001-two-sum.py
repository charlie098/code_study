class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_list = {} # 딕셔너리 생성 빠르게 검색 가능
        res = [] #결과용 리스트


        # 딕셔너리에 리스트값 넣기
        for i, x in enumerate(nums):
            temp = target - x # 주어진 값에서 i에 해당하는 x값을 빼서 저장

            if temp in dict_list: # 딕셔너리에 temp 값이 있나 확인
                idx1 = dict_list[temp] # 있으면 idx1을 딕셔너리서 빼오기
                idx2 = i # 값이 있는경우 idx2는 i와 동일
                res = [idx1, idx2] # 리스트에 저장
                return res #리스트를 반환

            dict_list[x] = i #없으면 딕셔너리에 x는 키 i는 밸류로 넣기 
        
        return res # 결과 리스트 반환

        
