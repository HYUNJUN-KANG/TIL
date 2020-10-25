```
headline = list(input())

for i in range(len(headline)):

    if 'a' <= headline[i] <= 'z':
        headline[i] = chr(ord(headline[i]-32))

print(''.join(headline))
```



_를 어떻게 처리해야할지 고민이었는데, 

`if 문에서 사용한 것과 같이 'a'와 'z'는 순서로 나타날 수 있는것 같다.`

`또한 list에서 하나씩 안 빼고도,  headline 리스트 안에 있는 index 값을 통하여 list 요소를 바꿀 수 있는 것도 중요하다.`

그렇게 한 뒤 join을 써서 문자열에 넣어줌으로써 끝냈다.





```
for tc in range(1, T-1):
    temp = input()

    year = temp[:4]
    month = temp[4:6]
    day = temp[6:]

    flag = True
    # 1 <= int(month) <= 12

    if int(month) <= 0 or int(month) >= 13:
        flag = False

    elif int(day) > day[int(month)] or int(day) <= 0:
        flag = False

    if flag:
        print("#{} {}/{}/{}".format(tc, year, month, day))
    else:
        print("#{} -1".format(tc))
```



달력도 마찬가지로 애초에 temp 값이 str으로 주어졌는데

### str도 index와 slicing이 가능하다.

이걸 까먹고 list로 만들려고 애먹었다,

그러므로 간편히 숫자 str 값에 int를 씌워줘서 정수로 만들어줬고,

그걸 이용하여 쉽게 비교할 수 있었다.



또한 조건문을 사용할때 `flag = True` 와 `False`를 통해 간편히 구분하자.



format 사용법을 익히자.

`print("#{} {}/{}/{}".format(tc, year, month, day))`



