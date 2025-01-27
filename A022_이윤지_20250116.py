# 주어진 통화 시간에 대해 두 가지 요금제(영식 요금제와 민식 요금제)를 각각 계산한 후, 더 저렴한 요금제를 출력하기

'''
1.주어진 통화 시간에 대해 두 가지 요금제를 각각 계산
2.두 요금제를 비교하여 더 저렴한 요금제 출력
3.요금이 같으면 "Y M"과 요금을 출력
'''

def solution():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 통화 개수와 통화 시간 입력
    N = int(data[0])  # 통화 개수
    times = list(map(int, data[1:]))  # 통화 시간 리스트

    # 영식 요금 계산
    y_cost = sum((time // 30 + 1) * 10 for time in times)

    # 민식 요금 계산
    m_cost = sum((time // 60 + 1) * 15 for time in times)

    # 요금 비교 및 출력
    if y_cost < m_cost:
        print(f"Y {y_cost}")
    elif y_cost > m_cost:
        print(f"M {m_cost}")
    else:
        print(f"Y M {y_cost}")

# 실행
solution()

#코드리뷰 
# if-elif-else문으로 조건에 맞게 출력을 잘 했음
