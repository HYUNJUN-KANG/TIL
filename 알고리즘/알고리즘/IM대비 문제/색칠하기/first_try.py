import sys
sys.stdin = open('input.txt', 'r')

def printArr(a):
    for lst in arr:
        print(*lst)
    print()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    cnt = 0

    # 색칠하기
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for x in range(r1, r2+1):
            for y in range(c1, c2+1):
                arr[x][y] += color

    for x in range(10):
        for y in range(10):
            if arr[x][y] == 3:
                cnt += 1

    print(cnt)