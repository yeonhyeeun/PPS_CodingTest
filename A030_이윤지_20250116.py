# 마르코프 체인(Markov Chain)을 활용하여 상태 전환 확률을 계산하기 ! 좋은 날 싫은 날~~

'''
1. 재현이의 기분은 좋은 날(0) / 싫은 날(1)로 나뉨
2. N일 뒤의 기분이 좋은 날일 확률과 싫은 날일 확률을 계산해야 함.
3. 기분 변화
    "좋은 날 → 좋은 날": p1
    "좋은 날 → 싫은 날": p2
    "싫은 날 → 좋은 날": p3
    "싫은 날 → 싫은 날": p4
4. 현재 상태를 바탕으로 N일 동안 확률을 반복적으로 계산


P(좋은날): 좋은 날일 확률
P(싫은날): 싫은 날일 확률
N=1: 초기 상태에서 하루만 지나면 확률 계산 가능
N>1: 이전 상태에서 새로운 상태를 반복 계산
'''

def solution():
    import sys
    input = sys.stdin.read
    data = input().split()

    # 입력 처리
    N = int(data[0])  # N일 뒤
    current_mood = int(data[1])  # 현재 기분 (좋은 날: 0, 싫은 날: 1)
    p1, p2, p3, p4 = map(float, data[2:])  # 확률 입력

    # 초기 상태 확률 설정
    P_good = 1 if current_mood == 0 else 0
    P_bad = 1 if current_mood == 1 else 0

    # N일 동안 상태 확률 계산
    for _ in range(N):
        new_P_good = P_good * p1 + P_bad * p3
        new_P_bad = P_good * p2 + P_bad * p4
        P_good, P_bad = new_P_good, new_P_bad

    # 결과 출력 (1000을 곱해 반올림)
    good_result = round(P_good * 1000)
    bad_result = round(P_bad * 1000)
    print(good_result)
    print(bad_result)

# 실행
solution()
