# 주어진 10개의 자연수 / 42의 나머지를 계산한 뒤, 서로 다른 나머지의 개수를 구하기

'''
1. 10개의 자연수를 입력받음
2. 각 숫자를 42로 나눈 나머지를 계산하여 저장
3. 나머지 값들을 집합(Set) 자료구조에 저장해 중복 제거
4. 집합의 크기를 계산하면 서로 다른 나머지 개수를 구할 수 있음

'''

def solution():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))

    # 42로 나눈 나머지 저장
    remainders = {x % 42 for x in data}

    # 서로 다른 나머지의 개수 출력
    print(len(remainders))

# 실행
solution()
