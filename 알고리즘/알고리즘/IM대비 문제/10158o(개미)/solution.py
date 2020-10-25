import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

# t의 시간을 가로와 세로를 따로 봄.
tx = t%(N*2)
ty = t%(M*2)

# 델타 처럼 만들기
dx = 1
dy = 1

# tx 시간만큼 이동
for i in range(tx):
    if x == N or x == 0:
        dx *= -1
    x += dx

# ty 시간만큼 이동
for i in range(ty):
    if y == M or y == 0:
        dy *= -1
    y += dy

print(x, y)
