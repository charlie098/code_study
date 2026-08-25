class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #이진 탐색 사용시 쉽게 해결되는 문제
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # 전부 돌아도 넣을 구간을 못찾으면 left 에 넣음 됨
        return left
            