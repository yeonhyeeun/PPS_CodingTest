#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 스킬트리 가능한 개수 구하는 문제

int solution(const char* skill, const char* skill_trees[], size_t skill_trees_len) {
    int answer = 0; // 가능한 스킬트리 개수

    // 스킬트리 순회
    for (size_t i = 0; i < skill_trees_len; i++) {
        int skill_index = 0; 
        bool is_valid = true; 

        // 각 스킬트리의 스킬 순서 검사
        for (size_t j = 0; skill_trees[i][j] != '\0'; j++) { 
            // 현재 스킬이 선행 스킬에 있는지 확인
            int found = -1; 
            for (int k = 0; skill[k] != '\0'; k++) {
                if (skill[k] == skill_trees[i][j]) { // 스킬 발견
                    found = k; 
                    break;
                }
            }

            // 현재 스킬이 선행 스킬에 포함되어 있는 경우
            if (found != -1) {
                // 순서 확인하기
                if (found == skill_index) {
                    skill_index++; // 다음 스킬로 이동
                } else { 
                    is_valid = false; // 순서가 틀림
                    break;
                }
            }
        }
        if (is_valid) {
            answer++;
        }
    }

    return answer; 
}
