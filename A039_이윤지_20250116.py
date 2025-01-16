# 입력받은 양의 정수가 완전제곱수인지 확인하기
#바이너리 서치 사용

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True  # 1은 완전 제곱수

        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
