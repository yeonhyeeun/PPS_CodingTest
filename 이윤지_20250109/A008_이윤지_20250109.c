#include <stdio.h>

int main() {
    int C; 
    scanf("%d", &C);

    while (C--) { 
        int N; // 학생 수
        int scores[1000]; // 점수
        int sum = 0; 
        int count = 0;

        // 학생 수 및 점수 입력 받기
        scanf("%d", &N);
        for (int i = 0; i < N; i++) {
            scanf("%d", &scores[i]);
            sum += scores[i]; 
        }

        // 평균 계산
        double avg = (double)sum / N;

        for (int i = 0; i < N; i++) {
            if (scores[i] > avg) {
                count++; // 평균 초과 학생 수 증가
            }
        }

        printf("%.3f%%\n", (double)count / N * 100);
    }

    return 0;
}
