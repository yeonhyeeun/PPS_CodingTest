#include <stdlib.h> 

// 1. 탐욕도 배열(g)와 쿠키 크기 배열(s)을 오름차순으로 정렬
// 2. 인덱스 초기화
// 3. 탐욕도와 쿠키 크기를 비교하면서 만족시키기
// 4. 만족한 아이의 수 반환

// 오름차순 정렬
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b); 
}

// 탐욕이 채워진 아이의 수
int findContentChildren(int* g, int gSize, int* s, int sSize) {
    
    qsort(g, gSize, sizeof(int), compare); // 탐욕도 정렬
    qsort(s, sSize, sizeof(int), compare); // 쿠키 크기 정렬

   
    int child = 0;   
    int cookie = 0;  

    
    while (child < gSize && cookie < sSize) {
        if (s[cookie] >= g[child]) { 
            child++; 
        }
        cookie++; 
    }

    return child;
}
