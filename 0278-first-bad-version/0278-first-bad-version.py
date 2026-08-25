# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # 오류가 난 지점을 찾는게 핵심
        # 이진 탐색을 해보면 빨리 찾음
        # 반 나누고 중앙값이 오류인지 체크
        # 중앙값이 오류라면 첫 오류는 본 값 또는 왼쪽에 존재
        # 중앙값이 오류가 아니면 첫 오류는 오른쪽에 있을 것

        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            
            # mid 버전이 불량(True)이면 최초 불량은 mid이거나 mid 왼쪽에 있음
            if isBadVersion(mid):
                right = mid
            # mid 버전이 정상(False)이면 최초 불량은 무조건 mid 오른쪽(mid + 1 이상)에 있음
            else:
                left = mid + 1
                
        # left == right가 되는 순간이 최초의 Bad Version
        return left