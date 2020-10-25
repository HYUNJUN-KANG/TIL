import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    print(li)
    selected = [0] * N
    result = set()
    result.add(0)

    powerset(selected, 0, 0)

    print("#{} {}".format(tc, len(result)))