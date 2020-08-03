import sys
sys.stdin = open('input.txt', 'r')

# test_case_1 = input()  # 첫번째 testcase
# value_test_case_1 = input()   # 첫번째 value
# test_case_2 = input()

# map_1 = map(int, value_test_case_1.split())

max_1 = 0
max_2 = 0
max_3 = 0
max_4 = 0

max_list = []





for k in range(10):
    test_case_1 = int(input())
    value_test_case_1 = input()
    map_1 = map(int, value_test_case_1.split())
    list_1 = list(map_1)
    sum_1 = 0

    for i in range(2, (test_case_1) - 2):


        if list_1[i] > list_1[i+1] and list_1[i] > list_1[i+2] and list_1[i] > list_1[i - 2] and list_1[i] > list_1[i - 1]:

            if list_1[i] - list_1[i+1] > list_1[i] - list_1[i+2]:

                max_1 = list_1[i] - list_1[i+2]


            if list_1[i] - list_1[i+1] <= list_1[i] - list_1[i+2]:

                max_2 = list_1[i] - list_1[i+1]

    # if abs(list_1[i] > list_1[i - 2]) and abs(list_1[i] > list_1[i - 1]):

            if list_1[i] - list_1[i - 1] > list_1[i] - list_1[i - 2]:
                max_3 = list_1[i] - list_1[i-2]

            if list_1[i] - list_1[i - 1] <= list_1[i] - list_1[i - 2]:
                max_4 = list_1[i] - list_1[i-1]
            max_list.append(max_4)
            max_list.append(max_3)
            max_list.append(max_2)
            max_list.append(max_1)

            min_min = 500

            for j in max_list:
                if j < min_min:
                    min_min = j
            sum_1 += min_min
    print(f'#{k+1} {sum_1}')
# print(test_case_1)     # 첫번째 testcase
#
# print(list(map(int, value_test_case_1.split( ))