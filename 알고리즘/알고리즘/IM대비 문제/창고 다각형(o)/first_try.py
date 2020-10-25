import sys
sys.stdin = open('input.txt', 'r')

n = int(input())

pillar = []
for i in range(n):
    l, h = map(int, input().split())
    pillar.append((l,h))
pillar.sort()

roof = [0] * (pillar[-1][0]+1)

for l,h in pillar:
    roof[l] = h

M = max(roof)
max_idx = roof.index(M)

height = 0
for left in range(max_idx):
    if height < roof[left]:
        height = roof[left]
    else:
        roof[left] = height
height = 0
for left in range(len(roof)-1, max_idx, -1):
    if height < roof[left]:
        height = roof[left]
    else:
        roof[left] = height
print(sum(roof))

