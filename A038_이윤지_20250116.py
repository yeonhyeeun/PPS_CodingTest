# 주어진 비음수 정수 x에 대해 정수 부분의 제곱근을 계산하기

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x  # 0 또는 1의 경우 바로 반환

        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:  # 정확히 x의 제곱근이면 반환
                return mid
            elif square < x:  # 제곱근이 더 큼
                left = mid + 1
            else:  # 제곱근이 더 작음
                right = mid - 1

        return right  # 정수 부분의 제곱근 반환
