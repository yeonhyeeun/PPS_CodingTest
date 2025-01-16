'''
정수 배열 nums이 주어졌을 때, 배열 안에서 모든 숫자는 두 번씩 나타나지만 하나의 숫자만 한 번 나타남. 이 한 번만 나타나는 숫자를 찾기

조건: 시간 복잡도 O(n)
    공간 복잡도는 O(1)  리스트나 딕셔너리 사용 불가)
'''
#배열의 모든 숫자를 순서대로 XOR 하면, 짝수 번 등장한 숫자는 모두 소거되고, 한 번만 등장한 숫자만 남게 됨

'''
XOR 연산(^)의 특징:
a ^ a = 0 (같은 숫자를 XOR하면 0)
a ^ 0 = a (0과 XOR하면 숫자가 그대로 유지됨)
교환 법칙, 결합 법칙 성립 (순서와 상관없이 연산 가능)

'''

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0  # XOR 연산의 초기값은 0
        for num in nums:
            result ^= num  # 배열의 모든 숫자를 XOR
        return result  # 최종적으로 남은 숫자가 정답
