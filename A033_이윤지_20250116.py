# 5명의 참가자가 얻은 점수의 합을 계산하고, 가장 높은 점수를 얻은 참가자의 번호와 점수를 출력하기

'''

1.각 참가자의 점수를 리스트로 저장
2.N=5, 각 참가자의 점수는 4개의 정수로 주어짐
3.sum(scores[i]): i-번째 참가자가 얻은 총점 계산
4.각 참가자의 총점 중 최대값과 해당 참가자의 번호를 찾음
5.winner: 최대 점수를 얻은 참가자의 번호
6.우승자의 번호와 점수를 출력

'''

def solution():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    max_score = 0
    winner = 0

    for i in range(5):  # 5명의 참가자
        scores = list(map(int, data[i].split()))  # 각 참가자의 점수
        total = sum(scores)  # 총점 계산
        if total > max_score:  # 최대 점수 갱신
            max_score = total
            winner = i + 1  # 참가자 번호는 1부터 시작

    print(winner, max_score)

# 실행
solution()
