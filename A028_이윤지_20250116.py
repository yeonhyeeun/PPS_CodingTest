# *** 두 정수 A와 B가 매우 큰 숫자일 수 있으므로, 일반적인 정수 자료형으로 처리할 수 없는 경우를 대비
'''
1, 두 정수를 문자열로 입력받아 정수형으로 변환
2. a + b 계산
3. 결과 출력 
'''

def solution():
    import sys
    input = sys.stdin.read
    # 두 정수를 입력받음
    A, B = map(int, input().split())
    # 두 정수의 합을 계산하고 출력
    print(A + B)
