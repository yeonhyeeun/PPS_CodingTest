# 정수 n이 4의 거듭제곱인지 확인하는 문제. n=4 x형태가 성립하면 True, 아니면 False를 반환함

'''
n을 4로 나누며 반복적으로 확인
n=1이 되면 4의 거듭제곱
'''

class Solution:
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1

