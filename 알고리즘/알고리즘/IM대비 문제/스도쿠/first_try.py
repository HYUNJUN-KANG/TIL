import sys
sys.stdin = open('input.txt', 'r')
T = int(input())

def solve():
    global flag

    # 행우선
    for i in range(9):
        visit = [0] * 10
        for j in range(9):
            visit[arr[i][j]] += 1
            if visit[arr[i][j]] > 1:
                flag = 0
                return

    # 열우선
    for i in range(9):
        visit = [0] * 10
        for j in range(9):
            visit[arr[j][i]] += 1
            if visit[arr[i][j]] > 1:
                flag = 0
                return

    # 3 X 3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            visit = [0] * (10)
            for x in range(3):
                for y in range(3):
                    visit[arr[i+x][j+y]] += 1
                    if visit[arr[i+x][j+y]] > 1:
                        flag = 0
                        return



for tc in range(1, T+1):
    flag = 1
    arr = [list(map(int, input())) for _ in range(9)]
    solve(arr)
