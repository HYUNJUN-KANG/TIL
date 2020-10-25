import sys
sys.stdin = open('input.txt', 'r')

def cal(a, i, b):
    a = int(a)
    b = int(b)

    if i == '+':
        return a + b
    elif i == '-':
        return a - b
    elif i == '*':
        return a * b
    elif i == '/':
        return a // b



T = int(input())

for tc in range(1, T+1):

    li_1 = list(input().split())
    li = li_1[0:len(li_1)-1]

    stack1 = []
    li_cal = ['+', '-', '*', '/']


    for i in li:
        if i not in li_cal:
            stack1.append(i)


        else:
            if len(stack1) < 2:
                print('#{} error'.format(tc))
                break

            b = stack1.pop()
            a = stack1.pop()
            stack1.append(cal(a, i, b))

    else:
        if len(stack1) != 1:
            print('#{} error'.format(tc))

        else:
            print('#{} {}'.format(tc, stack1[0]))
