#include <stdio.h>
#include <string.h>
#include <ctype.h> 

// 1. 문자열 길이가 4 또는 6인지 확인
// 2. 숫자로만 이루어졌는지 확인
// 3. 조건을 모두 만족하면 True 반환

int solution(const char* s) {
    int length = strlen(s); 

    if (length != 4 && length != 6) {
        return 0; 
    }

    for (int i = 0; i < length; i++) {
        if (!isdigit(s[i])) { // 숫자가 아닌 문자가 있으면
            return 0; // False 반환
        }
    }

    return 1; // True 반환
}

int main() {
    // 테스트
    printf("%d\n", solution("1234"));  
    printf("%d\n", solution("a234"));  
    printf("%d\n", solution("12345"));  
    printf("%d\n", solution("000000")); 
    return 0;
}
