#include <stdlib.h>

// 정수 배열에 1을 더한 결과 반환
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    for (int i = digitsSize - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i]++;
            *returnSize = digitsSize;
            return digits;
        }
        digits[i] = 0;
    }

    int* result = (int*)malloc((digitsSize + 1) * sizeof(int));
    result[0] = 1;
    for (int i = 1; i <= digitsSize; i++) {
        result[i] = 0;
    }
    *returnSize = digitsSize + 1;
    return result;
}

//코드리뷰 작성 📚 
//int* 타입을 반환하는 함수를 작성하는데 어려움이 없어 보이고 malloc과 sizeof 메서드를 잘 사용하는 것 같다! 
