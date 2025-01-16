'''

숫자 k개를 제거하면 남아야 할 숫자는 len(number)−k개임
스택을 이용해 숫자를 한 자리씩 확인하기
-스택의 마지막 숫자보다 현재 숫자가 더 크면, 스택에서 숫자를 제거 k개의 숫자를 제거하기 전까지 반복.
k개의 숫자를 모두 제거한 후에는 나머지 숫자를 순서대로 스택에 추가. 스택의 길이가 len(number)−k를 초과하지 않도록 유지.

'''

def solution(number, k):
    stack = []  # 결과를 저장할 스택
    for digit in number:
        # 스택이 비어있지 않고, 현재 숫자가 스택의 마지막 숫자보다 크고, 제거할 기회(k)가 남아 있다면 제거
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)  # 현재 숫자를 스택에 추가
    
    # 숫자를 모두 처리한 뒤 남은 k개 제거
    return ''.join(stack[:len(number) - k])
