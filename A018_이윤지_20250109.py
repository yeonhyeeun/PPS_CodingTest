# A를 재배열하여 S=A[0]×B[0]+⋯+A[N−1]×B[N−1]의 값을 최소화하기
'''
A를 오름차순 정렬 → 작은 값부터 사용
B를 내림차순 정렬 → 큰 값부터 사용

정렬된 A와 B를 순서대로 곱해 모두 더하면 S의 최솟값이 나옴

'''
def solution():
    # 입력 처리
    N = int(input())  # 배열의 길이
    A = list(map(int, input().split()))  # 배열 A
    B = list(map(int, input().split()))  # 배열 B

    # A는 오름차순 정렬, B는 내림차순 정렬
    A.sort()
    B.sort(reverse=True)

    # S 값 계산
    S = sum(A[i] * B[i] for i in range(N))
    
    # 결과 출력
    print(S)

# 실행
solution()

# 코드리뷰 
# list를 만들때 문제 조건에 맞게 split을 적절히 사용하였다  
