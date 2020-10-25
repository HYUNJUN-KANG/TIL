def calc(long, short):

    max_value = -9999999

    for i in range(len(long) - len(short)+1):
        result = 0
        for j in range(len(short)):
            result += long[i+j]*short[j]

        if max_value < result:
            max_value = result


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    numsA = list(map(int, input().split()))
    numsB = list(map(int, input().split()))

    if len(numsA) > len(numsB):
        ans = calc(numsA, numsB)
    else:
        ans = calc(numsB, numsA)

    print("#{} {}".format(tc, result)