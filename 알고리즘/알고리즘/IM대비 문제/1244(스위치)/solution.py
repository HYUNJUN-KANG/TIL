import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
arr = list(map(int, input().split()))
C = int(input())

for i in range(C):
    # 학생 성별과 학생 받은 수
    G, N = map(int, input().split())

    # 남학생 일때
    if G == 1:
        for i in range(N-1, len(arr), N):    # 인덱스 0을 맞추기 위해 -1
            arr[i] = arr[i]^1   # XOR 연산은 1^1 -> 0 /   0^1  -> 1

    # 여학생 일때
    else:
        N = N-1       # 인덱스 0으로 바꾸기 위해서
        arr[N] = arr[N]^1
        for i in range(1, min(len(arr)-N, N+1)):
            if arr[N+i] == arr[N-i]:  # 이렇게 비교할거니까 for 문은 arr을 돌리는게  아니라 1부터 돌려야함.
                arr[N+i], arr[N-i] = arr[N-i]^1, arr[N+i]^1
            else:
                break

    print(arr[0], end=' ')
    for i in range(1, len(arr)):
        if i%20 == 0:
            print()
        print(arr[i], end=' ')