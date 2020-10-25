import sys; sys.stdin = open('input.txt', 'r')

paren = {'(': ')', '{': '}', ')': '(', '}': '{'}

T = int(input())
for tc in range(1, T+1):
    arr = input()


    S = []
    # 한 문자씩 읽어서 처리
    ans = 1
    for ch in arr:
        # 여는 괄호 일 경우 push
        if ch == '(' or ch == '{':
            S.append(ch)
        # 닫는 괄호 일 경우
        elif ch == ')' or ch == '}':
            # 빈 스택일 경우
            if len(S) == 0:
                ans = 0; break
            t = S.pop()
            # ch와 S[-1] 비교해서 다르다.
            if paren != t
                ans = 0; break
            # 같다면 스택에 제거
            S.pop()

    # 빈스택인지 조사
    if len(S) != 0:
        ans = 0