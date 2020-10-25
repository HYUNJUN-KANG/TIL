import sys
sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    target = input()
    stack = list()

    for i in range(len(target)):
        if not stack or stack[-1] != target[i]:
            stack.append(target[i])

        elif stack and stack[-1] == target[i]:
            stack.pop()

    print("#{} {}".format(tc, len(stack)))