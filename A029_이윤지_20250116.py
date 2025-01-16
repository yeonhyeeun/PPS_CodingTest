'''
규칙 1: 문을 여는 방법은 두 가지(밀기, 당기기)이며, 연속된 두 문의 방법이 같을 수 없다
규칙 2: 2의 배수 번째 문은 동일한 방법으로 열어야 한다
규칙 3: 3의 배수 번째 문은 동일한 방법으로 열어야 한다
규칙 4: N번째 문이 N≥10일 경우, "탈출 불가능" 메시지를 출력한다

N≥10일 경우 탈출 불가능:
출력: "Love is open door"

N<10일 경우:

첫 번째 문을 연 방법(first)을 기준으로, 각 문에 대해 규칙에 맞게 결정
𝑖i-번째 문에서:
2의 배수와 3의 배수 조건을 만족하도록 설정
이전 문과 다른 방법으로 열림
규칙을 순차적으로 적용하여 각 문의 열기 방법을 결정

'''

# 규칙에 따라 문을 여는 방법을 결정해야 하는 문제

def solution():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])  # 총 문 개수
    first = int(data[1])  # 첫 번째 문의 열기 방법

    # N이 10 이상이면 탈출 불가능
    if N >= 10:
        print("Love is open door")
        return

    # 첫 번째 문 이후의 문 여는 방법 결정
    current = first
    for i in range(1, N):  # 두 번째 문부터 N번째 문까지
        # 연속되지 않도록 번갈아 열기
        current = 1 - current
        print(current)

# 실행
solution()
