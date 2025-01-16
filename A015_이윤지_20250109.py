#주어진 5개의 숫자를 각각 제곱한 후 합을 구하고, 이를 10으로 나눈 나머지를 계산하기
'''
1. 공백으로 구분된 5개의 숫자를 입력받음
2. 이 숫자들을 리스트에 저장
3. 입력받은 숫자들을 순회하며 각 숫자를 제곱
4. 제곱한 값을 모두 더함
5. 합을 10으로 나눈 나머지를 계산
6. 계산된 검증수를 출력
'''

# 입력받기
nums = list(map(int, input().split()))  # 공백으로 구분된 5개의 숫자 입력

# 각 숫자를 제곱한 뒤 합 계산
square_sum = sum(x ** 2 for x in nums)

# 검증수 계산 (합을 10으로 나눈 나머지)
verification_number = square_sum % 10

# 결과 출력
print(verification_number)
