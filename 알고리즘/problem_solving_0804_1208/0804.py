import sys
sys.stdin = open('input.txt', 'r')

T = 10



for tc in range(1, T+1):

    N = int(input())

    B = list(map(int, input().split( )))



    max_val = 0
    min_val = 10000


    for k in range(N):

        n = 0

        for i in B:

            if i > max_val:

                max_val = i
                max_index = n


            if i < min_val:
                min_val = i
                min_index = n
            n += 1
        max_val -= 1
        min_val += 1
        B[max_index] = max_val
        B[min_index] = min_val

    diff = max(B)-min(B)
    print(diff)