#include <stdio.h>

int main() {
    int arr[8]; 
    int ascending = 1; 
    int descending = 1;  

    // 입력 받기
    for (int i = 0; i < 8; i++) {
        scanf("%d", &arr[i]);
    }

    // 순서 확인
    for (int i = 0; i < 7; i++) {
        if (arr[i] < arr[i + 1]) { // 오름차순인지 확인
            descending = 0; // 내림차순 아님
        } else if (arr[i] > arr[i + 1]) { // 내림차순인지 확인
            ascending = 0; // 오름차순 아님
        }
    }

    // 결과 출력
    if (ascending) {
        printf("ascending\n");
    } else if (descending) {
        printf("descending\n");
    } else {
        printf("mixed\n");
    }

    return 0;
}
