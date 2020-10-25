import sys
sys.stdin =open('input.txt', 'r')

# 가로 세로
width, height = map(int, input().split())

# 잘라야 하는 갯수
N = int(input())

# 0 = 가로 / 1 = 세로

li = [list(map(int, input().split())) for _ in range(N)]

li_width = [0]
li_height = [0]

for i in range(N):
    if li[i][0] == 0:
        li_width.append(li[i][1])
    else:
        li_height.append(li[i][1])

li_width.append(height)
li_height.append(width)

a = sorted(li_width)
b = sorted(li_height)

max_width = 0
max_height = 0

for i in range(1, len(a)):
    width_val = a[i] - a[i-1]
    if max_width < width_val:
        max_width = width_val

for i in range(1, len(b)):
    height_val = b[i] - b[i-1]
    if max_height < height_val:
        max_height = height_val

print(max_width * max_height)