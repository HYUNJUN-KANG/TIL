import sys
sys.stdin = open('input.txt', 'r')

def search(target, pattern):
    for i in range(len(target)-len(pattern)+1):
        is_find = True
        for j in range(len(pattern)):
            if pattern[j] != target[i+j]:
                is_find = False
                break

        if is_find:
            return 1

    return 0

T = int(input())

for tc in range(1, T+1):
    n = input()
    tgt = input()

    result = search(tgt, n)

    print("#{} {}".format(tc, result))
