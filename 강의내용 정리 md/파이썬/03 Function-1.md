# 03 Function-1

![built_in](https://user-images.githubusercontent.com/18046097/61181739-2984fd80-a665-11e9-991b-f2f058397a69.png)



**내장함수 목록을 직접 볼 수도 있습니다.**

```python
dir(__builtins__)
```



## 함수의 `return`

앞서 설명한 것과 마찬가지로 함수는 반환되는 값이 있으며, 이는 어떠한 종류(~~의 객체~~)라도 상관없습니다.

단, **오직 한 개의 객체**만 반환됩니다.

함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.





## 매개변수(parameter) & 인자(argument)

### (1) 매개변수(parameter)

```python
def func(x):
      return x + 2
```

- `x` 는 매개변수(parameter)
- 입력을 받아 함수 내부에서 활용할 `변수`라고 생각하면 된다.
- 함수의 정의 부분에서 볼 수 있다.

### (2) 전달인자(argument)

```python
func(2)
```

- `2` 는 (전달)인자(argument)
- 실제로 전달되는 `입력값`이라고 생각하면 된다.
- 함수를 호출하는 부분에서 볼 수 있다.

> 주로 혼용해서 사용하지만 엄밀하게 따지면 둘은 다르게 구분되어 사용됩니다. 개념적 구분보다 함수가 작동하는 원리를 이해하는게 더 중요합니다.



ex) 원기둥의 부피

```python
def cylinder(r, h):
    area = r * r * 3.14
    volume = area * h
    return volume
```

### 기본 인자 값 (Default Argument Values)

함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있습니다.

------

**활용법**

```python
def func(p1=v1):
    return p1
```





### [연습] 기본 인자 값 활용

> 이름을 받아서 다음과 같이 인사하는 함수 `greeting()`을 작성하세요. 이름이 길동이면, "길동, 안녕?" 이름이 없으면 "익명, 안녕?" 으로 출력하세요.



```
# 아래에 greeting 함수를 작성하세요.
```



```
def greeting(name='익명'):           # 위치인자를 주지 않으면 익명을 씀.
    
    return f'{name}, 안녕?'
```



```
greeting('john')
```

```
'john, 안녕?'
```





```
greeting()
```

```
'익명, 안녕?'
```





### **주의\* 단, 기본 인자값(Default Argument Value)을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없습니다.**

In [ ]:

```
# 오류를 확인해봅시다.
```

In [28]:

```
def greeting(name='익명', grade):
    return f'{grade}학년 {name}님, 환영합니다.'
    
    
  File "<ipython-input-28-ebd673cdad03>", line 1
    def greeting(name='익명', grade):
                ^
SyntaxError: non-default argument follows default argument
```



해결하기 위해서는,

### 앞은 무조건, 뒤는 optional

```python
def greeting(grade, name='익명'):        # 앞은 무조건, 뒤는 optional
    return f'{grade}학년 {name}님, 환영합니다.'
```

```python
def greeting(age, grade=4, name='익명'):
    return f'{age}세 {grade}학년 {name}님, 환영합니다.'
```



### 키워드 인자 (Keyword Arguments)

키워드 인자는 직접 변수의 이름으로 특정 인자를 전달할 수 있습니다.



```
# 키워드 인자 예시
```



```
def greeting(age, name = '익명'):
    return f'{age}세 {name}님 환영합니다.'
```



```
# 호출 순서를 바꿔봅시다.
```

```
greeting('홍길동', 20)
```



# keyword argument는 다 쓰던지, 뒤에 쓰던지.

In [36]:

```
greeting(age=20, name='홍길동') # 순서 바꿔도 됌. # greeting(20, '홍길동')과 같음.
```

Out[36]:

```
'20세 홍길동님 환영합니다.'
```

In [38]:

```
greeting(name='홍길동', 20) #위치변수에 대하여 애매하므로 결과 오류.

  File "<ipython-input-38-26db3e825e00>", line 1
    greeting(name='홍길동', 20) #위치변수에 대하여 애매하므로 결과 오류.
                              ^
SyntaxError: positional argument follows keyword argument
```





```python
greeting(20, name='홍길동') # 부분적 키워드 argument는 뒤에 와야한다.
```



### 가변(임의) 인자 리스트(Arbitrary Argument Lists)

앞서 설명한 `print()`처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 가변 인자 리스트`*args`를 활용합니다.

가변 인자 리스트는 #`tuple` 형태로 처리가 되며, 매개변수에 `*`로 표현합니다.

------

#### 활용법

```python
def func(a, b, *args):
```

> `*args` : 임의의 개수의 위치인자를 받음을 의미
>
> 보통, 이 가변 인자 리스트는 매개변수 목록의 마지막에 옵니다.

In [65]:

```
def func(a, b, *args):
    print(type(a))
    print(type(b))
    print(type(args))
    print(args)
```

In [66]:

```
func(10, 20, 30, 40, 50, 60)
# a = 10
# b = 20
# args = (30, 40 ,50 ,60)
<class 'int'>
<class 'int'>
<class 'tuple'>
(30, 40, 50, 60)
```

In [ ]:

```
# 가변 인자 예시
# print문은 *obejcts를 통해 임의의 숫자의 인자를 모두 처리합니다.
```

In [40]:

```
print(1,2,3,4,5,6,7,8,9,10,11,12)
1 2 3 4 5 6 7 8 9 10 11 12
```

In [ ]:

```
# args는 tuple입니다.
```

In [52]:

```
def func(*args):
    for i in args:
        
        if i & 2 == 0:
            print(i)
    
func(1, 2, 3, 4, 5, 6)
2
3
6
```



### [연습] 가변 인자 리스트를 사용해봅시다.

> 정수를 여러 개 받아서 가장 큰 값을 반환(return)하는 함수 `my_max()`를 작성하세요.

```python
my_max(10, 20, 30, 50)
```

------

```
예시출력)
50
```

In [54]:

```
max(1, 2, 3, 4)

# 아래에 코드를 작성하세요.
```

Out[54]:

```
4
```

In [59]:

```
def my_max(*args):
    
    max_value = -sys.maxsize
    
    for i in args:
        if max_value < i:
            max_value = i
    return max_value
        
        
```

In [60]:

```
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
my_max(-1, -2, -3, -4)
```

Out[60]:

```
-1
```



### 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

정해지지 않은 키워드 인자들은 **`dict`** 형태로 처리가 되며, `**`로 표현합니다.

보통 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있습니다.

------

#### 활용법

```python
def func(**kwargs):
```

> `**kwargs` : 임의의 개수의 키워드 인자를 받음을 의미

우리가 dictionary를 만들 때 사용할 수 있는 `dict()` 함수는 [파이썬 표준 라이브러리의 내장함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이 구성되어 있습니다.

> ![dictionary](https://user-images.githubusercontent.com/18046097/61181740-2984fd80-a665-11e9-94cf-7f5ab41873b1.png)

In [68]:

```
def func1(**kwargs):
    print(type(kwargs))
    print(kwargs)
```

In [70]:

```
func1(name='ed', age='20', gender='male') # = 양 옆으로 띄어쓰기가 없다.
<class 'dict'>
{'name': 'ed', 'age': '20', 'gender': 'male'}
```

In [ ]:

```
# 딕셔너리 생성 함수 예시(키워드 인자)
```

In [61]:

```
#
hi = dict(한국어='안녕',영어='hi')
print(hi)
{'한국어': '안녕', '영어': 'hi'}
```



### [연습] 정의되지 않은 키워드 인자를 처리

> `my_dict()` 함수를 만들어 실제로 dictionary 모습처럼 출력 함수를 작성하세요.

------

```
예시 출력)
{'한국어': '안녕', '영어': 'hi', '독일어': 'Guten Tag'}
```

In [ ]:

```
# 아래에 코드를 작성한 뒤 호출하세요.
```

In [64]:

```
def my_dict(**kwargs):
    return kwargs      # b/c 딕셔너리이므로

my_dict(한국어='안녕')
```

Out[64]:

```
{'한국어': '안녕'}
```