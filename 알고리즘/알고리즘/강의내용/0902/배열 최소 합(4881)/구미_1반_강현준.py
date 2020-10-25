import sys
sys.stdin = open('input.txt', 'r')

def cal(idx, visited, sum):
    global min_value
    if idx >= N:
        if sum < min_value:
            min_value = sum
        return

    if sum > min_value:
        return

    for i in range(N):
        if visited[i] == 0:
            sum += li[idx][i]

            visited[i] = 1

            cal(idx+1, visited, sum)

            visited[i] = 0
            sum -= li[idx][i]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]

    visited = [0]*N

    sum = 0
    min_value = 99999

    cal(0, visited, sum)

    print("#{} {}".format(tc, min_value))