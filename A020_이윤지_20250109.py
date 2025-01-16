# 역마다 내리고 타는 사람 수를 순차적으로 처리하면서, 기차 안에 사람이 가장 많을 때의 인원 수를 계산하기

'''
1. 처음에는 기차 안에 사람이 0명임
2. 각 역에서 내리고 타는 사람 수를 순차적으로 처리하면서 기차 안의 현재 인원 수를 갱신
3. 현재 기차 안 인원 = 이전 인원 - 내린 사람 + 탄 사람
4. 계산 후, 현재 인원 수를 최대 인원 수와 비교하여 갱신
5. 각 역을 처리하며 기록한 최대 인원을 출력
'''

def solution():
    max_people = 0  # 기차 내 최대 인원 수
    current_people = 0  # 현재 기차 내 인원 수

    for _ in range(4):  # 4개의 역 처리
        out_people, in_people = map(int, input().split())  # 내린 사람, 탄 사람 입력
        current_people = current_people - out_people + in_people  # 현재 인원 계산
        max_people = max(max_people, current_people)  # 최대 인원 갱신

    print(max_people)  # 결과 출력

# 실행
solution()
