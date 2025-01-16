# 주어진 정수 num의 각 자릿수를 반복해서 더하고, 한 자리 숫자가 될 때까지 반복 후 결과를 반환하기

'''
1. 각 자릿수를 더하는 과정을 반복하여 한 자리 숫자가 될 때까지 진행
2. 자릿수를 구하려면 정수를 문자열로 변환하거나, 10으로 나누는 연산을 사용
'''

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = sum(int(digit) for digit in str(num))  # 각 자릿수를 더하기
        return num
