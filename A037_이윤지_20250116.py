'''
숫자의 각 자릿수 d에 대해 n%d==0이어야 함
숫자에 0이 포함되어서는 안 됨
'''

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(num):
            temp = num
            while temp > 0:
                digit = temp % 10
                # 자릿수가 0이거나, 나눠떨어지지 않으면 False
                if digit == 0 or num % digit != 0:
                    return False
                temp //= 10
            return True
        
        # 범위 순회 및 필터링
        result = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                result.append(num)
        
        return result
