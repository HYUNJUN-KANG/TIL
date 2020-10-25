import sys
sys.stdin = open('input.txt', 'r')

# 참외 개수
N = int(input())
li_width = []
li_height = []

for _ in range(6):
    idx, value = map(int, input().split())

    if idx == 1 or idx == 2:
        li_width.append(value)
    else:
        li_height.append(value)

a = sorted(li_width)
b = sorted(li_height)

small_val = max(a[0] * b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])

big_val = a[2] * b[2]
print(small_val)
result = (big_val - small_val) * N
print(result)

