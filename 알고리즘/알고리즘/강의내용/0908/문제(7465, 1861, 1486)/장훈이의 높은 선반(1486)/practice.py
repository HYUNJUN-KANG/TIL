import sys
sys.stdin = open('input.txt', 'r')

def tower(idx, tmp_sum):
    global min_height
    if tmp_sum > min_height:
        return

    if idx == N:
        if tmp_sum >= B and min_height > tmp_sum:
            min_height = tmp_sum
        return

    tower(idx + 1, tmp_sum + heights[idx])
    tower(idx + 1, tmp_sum)


T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    INF = float("inf")
    min_height = INF
    tower(0, 0)