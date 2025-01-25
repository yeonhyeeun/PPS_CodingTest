'''
문자열의 각 단어의 첫 문자는 대문자로 변환
나머지 문자는 모두 소문자로 변환
공백이 연속해서 나오는 경우에도 그 자리를 유지


1.입력 문자열 s를 공백을 기준으로 나누어 단어 목록을 생성
2.각 단어의 첫 문자를 대문자로 변환하고, 나머지는 소문자로 변환
3.공백이 연속으로 나오는 경우도 처리
4.변환된 단어들을 공백으로 연결하여 결과 문자열 생성
5.공백이 앞뒤로 있거나 연속된 공백을 처리하기 위해 split() 대신 split(" ") 사용
'''

def solution(s):
    # 공백을 포함한 문자열을 정확히 처리하기 위해 split(" ") 사용
    words = s.split(" ")
    
    # 각 단어를 변환
    converted_words = []
    for word in words:
        if word:  # 단어가 비어있지 않으면
            converted_words.append(word[0].upper() + word[1:].lower())
        else:  # 공백 유지
            converted_words.append("")
    
    # 공백으로 연결하여 결과 문자열 반환
    return " ".join(converted_words)
