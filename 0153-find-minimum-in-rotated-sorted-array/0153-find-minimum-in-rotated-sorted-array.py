class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 제한 시간이 log n 이라는거 유의할 것
        # 결국 해야 되는 일은 다르지 않음
        # 최소값을 반으로 나눠 찾아가면됨
        
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # mid 값이 맨 오른쪽 값보다 크면 최솟값은 무조건 오른쪽 구간에 있음
            if nums[mid] > nums[right]:
                left = mid + 1
            # mid 값이 맨 오른쪽 값보다 작거나 같으면 최솟값은 mid 또는 왼쪽 구간에 있음
            else:
                right = mid

        # left와 right가 만나는 지점이 최솟값의 인덱스
        return nums[left]