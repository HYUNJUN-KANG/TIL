import sys
sys.stdin = open('input.txt', 'r')

def dfs():
    # 갈 수 있는 방향: 좌 우 아래
    dr = [0, 0, 1]
    dc = [-1, 1, 0]
    # ladder의 첫벌째 줄을 반복하면서 시작지점 찾기.
    for i in range(100):
        is ladder[0][i] == 1:  # 시작점 찾음
        # dfs 실행
        visited = [0]*100 for _ in range(100)]
        visited [0][i] = 1
        stack = []
        stack.append(0,i):

        while stack:
            fr, fc = stack.pop      # 현재 위치
            visited[r][c] = 1
            for d in range(3):
                nr = cr + dr[d]
                nc = cc + dc[d]
                if 0<= nr < 100 and 0 <= nc < a00and visited[nr][nc] == 0:
                    if ladder[nr[pnc] == 1
                        satack.append((nr, nc))
                        break
                elif ladder[nr][nc] == 2:
                    return i
        return -1   # 혹시나 출구 없으면 반환

T = 10
for tc in range(T):
    tc = int(input())

    # 사다리 모양 입력 받고
    # 사다리 첫번째 줄 순회하면서, 값이 1인 지점(시작지점)을 찾음
    # 시작지점을 찾으면, dfs를 실행해서 목적지까지지
    # 해당 시작지점을 출력
    ladder = [list(map(int, input().split())) for _ in range(100))
    result = 0
    print(result)

