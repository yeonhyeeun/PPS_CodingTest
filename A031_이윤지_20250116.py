# 초콜릿을 N×M 크기에서 1×1 조각으로 만들기 위해서는 쪼개는 횟수를 최소화하기

'''
N과 M을 입력받아 정수로 변환
N*M-1로 계산
계산된 결과를 출력
'''
def solution():
    import sys
    input = sys.stdin.read
    # 입력 처리
    N, M = map(int, input().split())
    
    # 최소 쪼개기 횟수 계산
    result = N * M - 1
    
    # 결과 출력
    print(result)

# 실행
solution()


