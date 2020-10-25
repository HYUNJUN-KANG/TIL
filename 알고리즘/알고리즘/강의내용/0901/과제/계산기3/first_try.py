import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    sen = input()
    cal = ['+', '*']
    cal_1 = ['(', ')']
    li = []
    stack = []


    def calculation(x):
        if x == '*':
            return 1
        elif x == '+':
            return 0
        elif x == '(' or x == ')':
            return -1


    for i in sen:
        if i not in cal and i not in cal_1:
            li.append(int(i))
        elif i in cal:
            while len(stack) > 0:
                if calculation(stack[-1]) <= calculation(i):
                    break
                li.append(stack.pop())
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while True:
                x = stack.pop()
                if x == '(':
                    break
                li.append(x)
    for i in li:
        if i not in cal and i not in cal_1:
            stack.append(i)
        elif i == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1 + n2)
        elif i == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n1 * n2)
    print('#{} {}'.format(tc, stack[0]))