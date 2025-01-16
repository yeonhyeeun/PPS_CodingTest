'''
str(x)로 숫자를 문자열로 변환
각 자릿수를 int(digit)로 변환하여 합산
x % digit_sum == 0이면 True 반환
그렇지 않으면 False 반환
'''

def solution(x):
    # 자릿수 합 계산
    digit_sum = sum(int(digit) for digit in str(x))
    
    # 하샤드 수 판별
    return x % digit_sum == 0
