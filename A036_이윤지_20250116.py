#주어진 숫자 배열에서 홀수 번 등장한 숫자들을 모두 XOR한 결과를 구하기

def solution():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])  # 테스트 케이스 수
    results = []
    idx = 1

    for t in range(1, T + 1):
        N = int(data[idx])  # 현재 테스트 케이스의 숫자 개수
        numbers = map(int, data[idx + 1].split())
        idx += 2

        # XOR 계산
        xor_result = 0
        for num in numbers:
            xor_result ^= num

        # 결과 저장
        results.append(f"Case #{t}\n{xor_result}")

    # 결과 출력
    print("\n".join(results))

# 실행
solution()
