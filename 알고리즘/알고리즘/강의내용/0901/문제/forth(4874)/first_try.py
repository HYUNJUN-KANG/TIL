import sys
sys.stdin = open('input.txt', 'r')

def cal(target):
    global result
    result = 0
    for i in target:
        if i not in li_cal:
            stack1.append(i)

        elif len(stack1) == 0:
            stack_result.append(i)
            cal(stack_result)

        else:
            # if result:
            #     stack1.append(result)

            a = stack1.pop()
            b = stack1.pop()

            if i == '+':
                result = a + b
            elif i == '-':
                result = a - b
            elif i == '*':
                result = a * b
            elif i == '/':
                result = a / b
            elif i == '.':
                return result
            else:
                cal(target[target.index(i)::])
            stack_result.append(result)

    return result

T = int(input())

for tc in range(1, T+1):

    li = list(input().split())

    target = []

    li_cal = ['+', '-', '*', '/', '.']


    cnt_cal = 0
    cnt_value = 0



    for i in li:
        if i not in li_cal:
            target.append(int(i))
            cnt_value += 1

        else:
            target.append(i)
            cnt_cal += 1

    if cnt_value < cnt_cal:
        result = 'error'

    else:
        stack1 = []
        stack_result = []

        cal(target)
    #     stack1 = []
    #
    #     for i in target:
    #         if i not in li_cal:
    #             stack1.append(i)
    #         else:
    #             if result:
    #                 stack1.append(result)
    #
    #             a = stack1.pop()
    #             b = stack1.pop()
    #
    #             if i == '+':
    #                 result = a + b
    #             elif i == '-':
    #                 result = a - b
    #             elif i == '*':
    #                 result = a * b
    #             elif i == '/':
    #                 result = a / b
    #             else:
    #                 print(result)
    # print(result)






