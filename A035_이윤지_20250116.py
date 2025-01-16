'''
1.테스트 케이스 개수 
2.T와 T개의 수학식을 입력받음.
3.각 식은 첫 번째 숫자와 연산자들이 공백으로 구분됨.
4.식의 첫 번째 숫자를 초기값으로 설정.
5.연산자를 순서대로 읽으며, 해당 규칙(@, %, #)에 따라 값을 갱신.
6.계산된 결과를 소수점 둘째 자리까지 출력.
'''
def solution():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])  # 테스트 케이스 수
    results = []

    for i in range(1, T + 1):
        tokens = data[i].split()
        value = float(tokens[0])  # 첫 번째 숫자

        # 연산자 처리
        for op in tokens[1:]:
            if op == "@":
                value *= 3
            elif op == "%":
                value += 5
            elif op == "#":
                value -= 7

        # 결과 저장 (소수점 둘째 자리까지)
        results.append(f"{value:.2f}")

    # 출력
    print("\n".join(results))

# 실행
solution()
