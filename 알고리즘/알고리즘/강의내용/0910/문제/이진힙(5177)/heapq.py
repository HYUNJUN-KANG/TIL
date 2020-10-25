from heapq import heapify

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    heapify(arr)

    v = (N -1)