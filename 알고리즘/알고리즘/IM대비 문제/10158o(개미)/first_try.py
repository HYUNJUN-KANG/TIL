import sys
sys.stdin = open('input.txt', 'r')

w, h = map(int, input().split())
li = [[0] * (w+1) for _ in range(h+1)]

sw, sc = map(int, input().split())

r = h - sc
c = sw
t = int(input())

for i in range(t % 12):
    r -= 1
    if r > h+1:
        r -= 2
    elif r < 1:
        r += 2

    c += 1
    if c > w+1:
        c -= 2
    elif c < 1:
        c += 2

print(r, c)
