# 다솜이의 방 번호에 포함된 각 숫자를 세고, 플라스틱 숫자 세트를 최소한으로 사용하여 필요한 숫자를 만들도록 계산하기
'''
1. 방 번호를 문자열로 변환해 각 문자를 순회하며 숫자별 빈도를 센다
2. 6과 9는 합쳐서 처리한 뒤, 올림 계산으로 필요한 개수를 구한다
3. 나머지 숫자는 빈도 그대로 사용한다
4. 모든 숫자에 대해 최댓값을 찾아 출력한다
'''
import math

def solution(N):
    # 숫자별 카운트
    count = [0] * 10  # 0~9의 숫자 개수를 담을 배열
    for digit in str(N):
        count[int(digit)] += 1

    # 6과 9는 합쳐서 처리 (올림 계산)
    count[6] = math.ceil((count[6] + count[9]) / 2)
    count[9] = 0  # 이미 9랑 6을 합쳤으니 초기화

    # 필요한 세트의 최댓값 반환
    return max(count)

# 입력
N = int(input())
# 결과 출력
print(solution(N))
