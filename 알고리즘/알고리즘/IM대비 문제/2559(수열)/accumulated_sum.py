import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
data = list(map(int, input().split()))

max_t = -999999999999
for i in range(1, N):
    data[i] += data[i-1]
data.append(0)   # i = K-1 일때 인덱스 -1이 되는걸 방지
for i in range(N-1, K-2, -1):
    data[i] -= data[i-K]
    if data[i] > max_t:
        max_t = data[i]

print(max_t)