num = int(input())

li = [[0]*100 for _ in range(100)]

for i in range(num):
    a, b = map(int, input().split())

    for r in range(a, a+10):
        for c in range(b, b+10):
            li[r][c] = 1

area = 0
for i in range(100):
    for j in range(100):
        area += li[i][j]

print(area)