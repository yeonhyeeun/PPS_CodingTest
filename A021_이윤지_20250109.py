# 여러 개의 멀티탭이 주어질 때, 최대한 많은 컴퓨터를 전원에 연결할 수 있는 개수 계산하기

def solution():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])  # 멀티탭 개수
    plugs = list(map(int, data[1:]))  # 각 멀티탭의 플러그 수
    
    # 최대 연결 가능한 컴퓨터 수 계산
    max_computers = sum(plugs) - (N - 1)
    
    # 결과 출력
    print(max_computers)

# 실행
solution()
