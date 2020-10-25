import sys
sys.stdin = open('input.txt', 'r')

c, r = map(int, input().split())
k = int(input())
total = c*r

if k == 1:
    print(1, 1)

if k > c*r:
    print(0)
else:
    concert = [[0]*c for _ in range(r)]
    cnt = 1
    y, x = r - 1, 0
    concert[y][x] = cnt

    while total - cnt >= 0:
        for dy, dx in [(-1,0), (0,1), (1,0), (0,-1)]:
            while 0 <= y + dy < r and 0 <= x + dx < c and concert[y+dy][x+dx] == 0:
                cnt += 1
                concert[y + dy][x + dx] = cnt
                y += dy
                x += dx
                if cnt == k:
                    print(x + 1, y + r)

    for r in concert:
        print(*r)
# 위, 오른쪽, 아래, 왼쪽