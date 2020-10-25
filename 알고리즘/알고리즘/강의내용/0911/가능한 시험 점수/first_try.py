import sys
sys.stdin = open('input.txt', 'r')

def powerset(selected, idx, sum):
    global result
    if idx == N:
        for i in range(N):
            if selected[i] == 1:
                result.add(sum)
        return
    if idx > N:
        return

    selected[idx] = 1
    powerset(selected, idx + 1, sum + li[idx])
    selected[idx] = 0
    powerset(selected, idx+1, sum)

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