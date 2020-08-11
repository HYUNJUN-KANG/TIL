import sys
sys.stdin = open('input.txt', 'r')

for j in range(1, 11):

    test_case = int(input())
    value_test_case = list(map(int, input().split()))
    sum_test_case = 0

    for i in range(2, len(value_test_case)-2):

        max_test_case = max(value_test_case[i+1], value_test_case[i+2], value_test_case[i-1], value_test_case[i-2])

        if value_test_case[i] > max_test_case:

            sum_test_case += value_test_case[i] - max_test_case

    print(f'#{j} {sum_test_case}')