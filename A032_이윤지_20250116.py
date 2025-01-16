#규칙을 따르는 아파트에서 k층 n호에 사는 사람의 수를 구하

'''
아파트의 사람 수 계산은 0층부터 시작하여, 각 층의 각 호에 사는 사람 수를 반복적으로 계산
k층 n호의 사람 수는 이전 층의 값을 반복적으로 더하는 방식으로 구함

동적 계획법(dp)은 큰 문제를 작은 문제로 나누어 그 결과를 활용해 큰 문제를 효율적으로 해결하는 알고리즘 설계 기법
이 방법은 반복되는 하위 문제를 풀 때 중복 계산을 피하기 위해 사용
'''

def solution():
    
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])  # 테스트 케이스 수
    results = []
    index = 1
    
    # 최대 k층, n호까지 계산하기 위한 DP 테이블
    max_k, max_n = 14, 14
    dp = [[0] * (max_n + 1) for _ in range(max_k + 1)]

    # 0층 초기화
    for n in range(1, max_n + 1):
        dp[0][n] = n

    # 나머지 층 계산
    for k in range(1, max_k + 1):
        for n in range(1, max_n + 1):
            dp[k][n] = dp[k][n - 1] + dp[k - 1][n]

    # 각 테스트 케이스 처리
    for _ in range(T):
        k = int(data[index])
        n = int(data[index + 1])
        index += 2
        results.append(dp[k][n])

    # 결과 출력
    for result in results:
        print(result)

# 실행
solution()
