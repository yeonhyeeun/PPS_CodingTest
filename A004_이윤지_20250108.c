#include <stdlib.h> 

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */


// 파스칼의 삼각형 생성 함수
int** generate(int numRows, int* returnSize, int** returnColumnSizes) {

    *returnSize = numRows;

    int** result = (int**)malloc(numRows * sizeof(int*)); // 행 크기 할당
    *returnColumnSizes = (int*)malloc(numRows * sizeof(int)); // 각 행의 열 크기 저장 배열 할당

    for (int i = 0; i < numRows; i++) {
        (*returnColumnSizes)[i] = i + 1;
        result[i] = (int*)malloc((i + 1) * sizeof(int));

        // 첫 번째와 마지막 요소는 항상 1
        result[i][0] = 1; 
        result[i][i] = 1; 

        // 위 두 값의 합
        for (int j = 1; j < i; j++) {
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j];
        }
    }

    return result;
}

//코드리뷰 작성 📚 
//지난번 파스칼 삼각형에 이어서 비슷한 문제인데 다르게 풀이하는 것이 인상적이고 바로 type이 int**인 함수를 짤 생각을 한 것이 신기하다. 
