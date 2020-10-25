import sys
sys.stdin = open('input.txt', 'r')

def bfs(r, c):
    visited[r][c] = 0
    queue = [(r, c)]


    while len(queue) > 0:
        r, c = queue.pop(0)

        if li[r][c] == 3:
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 9999 and li[nr][nc] != 1:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
            else:
                continue

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    li = [[] for _ in range(N)]


    for i in range(N):
        li_new = input()
        for j in range(N):
            li[i].append(int(li_new[j]))


    for i in range(N):
        for j in range(N):
            if li[i][j] == 2:
                r = i
                c = j
            if li[i][j] == 3:
                er = i
                ec = j

    # 좌 우 상
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[9999]*N for _ in range(N)]
    bfs(r, c)

    if visited[er][ec] == 9999:
        visited[er][ec] = 1

    print("#{} {}".format(tc, visited[er][ec]-1))



