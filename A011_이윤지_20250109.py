def solution(N, stages):
    # 스테이지별 실패율 저장
    failure_rates = []
    
    total_players = len(stages)
    
    for stage in range(1, N + 1):
        not_cleared = stages.count(stage)
        
        # 실패율 계산
        if total_players > 0:  
            failure_rate = not_cleared / total_players
        else:  # 도달한 사용자가 없는 경우
            failure_rate = 0
        
        # 실패율, 스테이지 번호 저장
        failure_rates.append((stage, failure_rate))
        
        # 다음 스테이지로 넘어가기
        total_players -= not_cleared

    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    
    # 정렬gn 스테이지 번호 추출
    result = [stage for stage, _ in failure_rates]
    return result
