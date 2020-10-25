import sys
sys.stdin = open('input.txt', 'r')

def check(target):
    stack = list()
    for i in range(len(target)):
        if target[i] == "(" or target[i] == "[" or target[i] == "{":
            stack.append(target[i])

        elif target[i] == ")" or target[i] == "]" or target[i] == "}":
            if len(stack) == 0:
                return 0
            else:
                tmp = stack.pop()
                if target[i] == ")" and tmp == "(":
                    continue
                elif target[i] == "]" and tmp == "[":
                    continue
                elif target[i] == "}" and tmp == "{":
                    continue

                return 0

    if len(stack) != 0:
        return 0
    else:
        return 1


T = int(input())

for tc in range(1, T+1):
    target = input()
    print("#{} {}".format(tc, check(target)))

