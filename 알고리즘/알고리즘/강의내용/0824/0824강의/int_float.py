str = "123"
str2 = "12.3"

test = "1+2"
print(test)             # 1+2
print(repr(test))       # '1+2'가 나옴
print(eval(test))       # 계산을 해버려서 3 나옴
print(eval(repr(test)))     # 1+2가 나옴 b/c '1+2'상태에서 계
print(eval(eval(repr(test)))) # 3나옴
