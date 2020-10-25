import sys
sys.stdin = open('input.txt', 'r')

def powerset(selected, idx, sum):
    global min_value

    if sum >= min_value:
        return

    if idx == N:
        if sum >= B:
            min_value = sum
        return

    selected[idx] = 1
    powerset(selected, idx + 1, sum + li[idx])
    selected[idx] = 0
    powerset(selected, idx + 1, sum)

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())

    li = list(map(int, input().split()))
    new_li = []
    selected = [0] * N
    min_value = 9999999
    powerset(selected, 0, 0)

    print("#{} {}".format(tc, min_value-B))