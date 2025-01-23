def solution(s):
    # 문자열의 길이가 1 
    if len(s) == 1:
        return 1

    min_length = len(s)
    
    # 2까지 
    for step in range(1, len(s) // 2 + 1):
        compressed = ""  # 압축 결과 
        prev = s[:step]  # 첫 번째 단위
        count = 1        # 반복

        for j in range(step, len(s), step):
            if s[j:j + step] == prev:  # 현재 단위가 이전 단위와 같으면
                count += 1             # 반복 횟수 증가하기
            else:                      # 다른 단위가 나오면
                if count > 1:          # 반복일 경우 반복 횟수와 함께 저장
                    compressed += str(count) + prev
                else:                  # 반복이 아니면 그대로 저장
                    compressed += prev
                prev = s[j:j + step]  
                count = 1            
        
        if count > 1:
            compressed += str(count) + prev
        else:
            compressed += prev

        min_length = min(min_length, len(compressed))
    
    return min_length

#코드리뷰 작성 📚
#15행의 코드 중 배열 안 식은 처음 보는 형식이어서 이런 부분은 찾아서 공부해야겠다고 느꼈다.
