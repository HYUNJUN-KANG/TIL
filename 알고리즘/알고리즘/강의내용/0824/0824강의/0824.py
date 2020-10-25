# 숫자를 하나씩 분리할 때는 % moular 연산 사용

123 // 10 >>> 12     //  10 >>> 1     // 10 >> 0
123 % 10 >>> 3     >>  2             >> 1


123 % 100 >>> 23
123 // 100 >> 1
23 % 10 >> 3
23 // 10 >> 2
3 % 10 >> 1
3 // 10 >> 3


def itoa(number):
    #해야할 일: 숫자를 한자리씩 잘라서 문자열로 만들기
    # 123 >> 123//100  >> 23//10     >> 3//1 -> 각각의 몫을 합치면 완성

    # 자리수(divider)를 알아야 한다.
    # 1. 자리수 구하고,
    # 2. 원래 숫자를 1에서 구한 수로 나누어 몫을 취해서 문자열에 추가한다.
    # 3. 숫자를 자리수로 나눈 나머지를 숫자로 정한다.
    # 4. 대상숫자가 0이 될 때까지 1~3을 반복한다.


    divider = 1 #
    # 1. divider 구하기
    while True:
        tmp = divider * 10
        if tmp > number:
            break
        divider = tmp

    # divider를 구했으니, 숫자를 나눠주자
    # 몫을 계속해서 문자열에 추가 해 줄거니까, 몫이 없을 때까지 반복

    while number > 0:
        quotient = number // divider
        remain = number % divider
        # 몫을 문자열로 만들어서 더해주기
        result += chr(quotient+48)
        number = remain
    return result

a = 12345
b = itoa(a)
print(b)