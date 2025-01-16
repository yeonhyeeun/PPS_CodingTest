# 세 자연수 A,B,C의 곱셈 결과에서 0부터 9까지의 숫자가 몇 번 사용되었는지를 구하기

'''

1. A×B×C를 계산
2. 곱셈 결과를 문자열로 변환
3. 0부터 9까지의 숫자가 문자열에서 몇 번 등장했는지 센다
4. 0부터 9까지의 빈도를 한 줄씩 출력.
'''

def solution():
    # 입력 받기
    A = int(input())
    B = int(input())
    C = int(input())
    
    # 곱셈 결과 계산
    result = A * B * C
    
    # 결과를 문자열로 변환
    result_str = str(result)
    
    # 0부터 9까지 등장 횟수 계산
    for i in range(10):
        print(result_str.count(str(i)))

# 실행
solution()
