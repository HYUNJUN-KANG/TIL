# Dynamic web 

사용자의 요청에 따라 다른 데이터를 보여줌



# Static web

: 어떠한 요청을 해도 이미 정리된 데이터를 보여줌





| MVC 패턴   | django                    |
| ---------- | ------------------------- |
| Model      | Model (데이터관리)        |
| View       | Template(인터페이스 화면) |
| Controller | View(중간관리(상호동작))  |



## django how

1) HTTP Request

2) URLS (url.py)

3) View (views.py)

4) Template (<filename>.html)

5) HTTP Response (HTML)



# 코드 작성 순서 - 데이터 흐름(url - view - template)

1. urls.py

2. views.py

3. templates

   



# Django

Django 3.1

`pip list`로 확인 가능



### 장고 설치하기

```python
pip install django

#특정 버전으로 받고 싶다
pip install django=3.0.8
```



### 장고 시작하기



#### 0) 프로젝트 만들기

```python
django-admin startproject first_webex
```

=> 'first_webex'라는 이름으로 폴더가 생성.

  * 여기 안에는 first_webex 폴더와 manage.py 생성 되어짐.
    * first_webex: 프로젝트 설정 파일들이 들어있음.
    * manage.py: 장고 명령어를 실행하기 위한 파일.
      * `python manage.py` : 장고명령어





#### 1) 프로젝트 시작:

#### `django-admin startproject first_project`

* 가장 바깥에 있는 폴더명은 수정 가능하나, setting 파일이 들어있는 폴더명은 건들이면 안된다.

#### 2) `cd first_project/` 로 접근 for manage.py 찾으러



#### 3) manage.py가 있는지 확인하기 위하여 `ls`로 확인한다.



#### 4) 장고 실행하기: `python manage.py runserver`



#### python manage.py startapp articles



* 장고는 application의 집합체로 동작

  * 실제로 어떠한 역할을 해주는 친구가 바로 app이다.

  * 하나의 프로젝트는 여러개의 app을 가질 수 있다.

    * 어플리케이션: 하나의 역할 및 기능 단위로 쪼개진 형태.

      * 회원관리/ 글 작성, 수정, 글 삭제/ 데이터를 수집 분석/ ....

      * 어플리케이션을 이렇게 나뉘어야 한다 같은 기준은 존재 X

      * 작은 프로젝트라면 어플리케이션을 따로 나누지 않아도 된다.

        

#### 5) 어플리케이션 생성

```python
python manage.py startapp 앱이름(복수형)
```

* 해당 앱 이름으로 폴더가 생성됨.

  #### * 앱을 생성하고 바로 settings.py로 가서 INSTALLED_APPS에 내가 생성한 파일을 등록해줘야 한다!!!! *

* installed_app에 가장 윗줄에 등록해준다.

* language_code = 'ko-kr' 대/소문자 지키기

* time_zone = 'Asia/Seoul'



### -----------------------------장고 실행하기 위한 단계---------------------------------







### -----------------------------서버 실행하기 위한 단계---------------------------------



# @@@@@@@@@@@@MTV 패턴 (MVC 패턴) 중요@@@@@@@@@@@@@

* Model: 장고에서는 Model - DB
* View: 장고에서는 Template - 보여지는 HTML
* Controller: 장고에서는 View - 동작 컨트롤



```python
UESR -  (request) - Server

url - (req)  -> urls.py

url 패턴을 보고 urls.py 가 views.py에 전달 for 해당동작 실행

views.py (controller) 가 필요할시 model(DB) 가져옴

Template(view(html)) 가져옴

render해서 response to user
```



### 우리가 가장 밀접하게 수정하여야 하는 파일명

1. urls.py
2. views.py
3. templates (html 틀)
4. models.py





### urls.py

```python
from articles(app 이름) import views

urlpatterns = [
    path('index/', views.index),
]
```

**path('url 패턴/',) 실행이 되어야 하는 views에 있는 함수, 해당 path의 별명) **

* 많이 놓치는 부분: URL 패턴 뒤에 슬래시!!!!!!







### views.py

```python
def index(request):        #django에서는 무조건 request를 인자로!!!!
    return render(request, 'index.html')
```

* 함수를 정의 (첫번째 인자로 request 필수!!!!!)

* return은 꼭 필요.

  * render: 주로 template과 함께 response 할 때 사용되는 함수

    

#### -Template Variable-

* render() 세번째 인자로 {'key': value}와 같이 딕셔너리 형태로 넘겨주면 template에서 key를 이용하여 value를 가져올 수 있다.
* html과 같은 template에서 views.py에서 준비한 변수를 가져다 쓰는 방법



```python
return render(request, 'index.html'), {'key': value}

or

context = {
    'key': value,
}

return render(request, 'index.html', context)
```

```python
{{ key }} 이렇게 value를 보여줄 수 있다.
```



## -JSON 반복문-

: 파이썬의 딕셔너리와 구조가 똑같다 (key: value)

단, 차이점은 json은 binary 형식으로 저장된다. (문자열로 저장이 된다.)

# ',' 잊지 말기!!!!

json 형식은 trailing comma가 허용되지 않음.





## Variable routing

: url 주소 일부를 변수처럼 사용해서 동적인 주소를 만드는 것.

​	주소요청: `http://127.0.0.1:8000/hello/문자열`



### template에서 해야할 일

* 폴더 명은 반드시 `templates`인 것을 확인

  



### -----------------------------여기 까지 기본 수정할 파일을 조작하는 방법---------------------------------



### -----------------------------여기서 본격 장고 동작 정의 방법---------------------------------



### urls.py

```python
path('hello/<str(타입):name(저장되는 변수명)>/')
```

* int: 숫자 형식으로 받음.

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('intro/', views.lotto),
]
```



### views.py

```python
def hello(request, name(저장되는 변수명)):
    print(name)
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)
```



### template (hello.html)

```html
<body>
	이름은 : {{ name }}  # context의 key값을 사용하면 value를 출력한다.
</body>
```



# Django Template Language (DTL)

* django template system에서 사용하는 built-in template.system이다.
* 조건, 반복, 치환, 필터, 변수 등의 기능을 제공
* 프로그래밍적 로직이 목적이 아니라 데이터를 표현하기 위한 것.
* 파이썬처럼 if, for를 사용할 수 있지만 이거는 단순히 phthon code로 실행되는 것이 아님.



###  템플릿 시스템 설계 철학

* django는 템플릿 시스템이 표현을 제어하는 도구이자 표현에 관련된 로직일뿐이라고 생각한다.
* 템플릿 시스템에서는 이러한 기본목표를 넘어서는 기능을 지원해서는 안된다.



### syntax (조건 반복문을 제공)

* 로직을 표현 할 때는: `{% for %}` 
* 값을 표현 할 때는: `{{  }}`
* 주석으로 나타내고 싶을 때는: `{#  #}`
* 여러줄 주석 `{% comment %} 문장 {% comment %}`



* for 태그

  * 반복을 위한 태그

  ```html
  {% for 임시변수 in iterable 한 객체 %}
  {% endfor %}
  ```

  

  * forloop.counter0 (index가 0부터 시작)

  ```html
  {% for post in posts %}
  	<p>{{ forloop.counter0 }}번 글 : {{ post }}</p>
  {% endfor %}
  ```

  

* for empty

  ```python
  {% for 임시변수 in iterable 한 객체 %}
  	값이 하나라도 있으면 여기가 실행됨.
  {% empty %}
  	출력할 값이 없으면 출력한다.
  {% endfor %}
  ```



* if 태그

  * 조건을 구분하기 위한 태그

  ```html
  {% if 조건문 %}
  {% elif 조건문 %}
  {% else %}
  {% endif %}
  ```



* 나머지 기타 유용한 DTL은 문서를 참고 (구글에 `django built in template`  검색)

  

* variable: `{{  }}`

* filter: `{{ variablefilter }}`

* tags: `{% tag %}`





## form

* HTML form tag 의미
* 입력 받은 데이터를 어딘가로 보낼 때 사용.

```html
#action: 보내려는 목표 # method: http method(get/ host)

<form action="/ / " method="GET">    # action 안에 //!!!!!!  # GET: 주소에 query string 형식으로 데이터를 전달하는 방식 (정보 조회할때 사용)
    
    # input 데이터를 입력 받게 적절히 코딩 하면 된다.
    
    <label for="name">데이터 입력 : </label>
 
    # 오락실 버튼
    <input type="button" id='name' name="name">
    
    # 미사일 버튼
    <input type="submit">
    		or
    <button></button>
</form>
```

```html
<form action="/catch/" method="GET">
      <label for="name">데이터 입력 : </label>
      <input type="text" id='name' name="name">
      <label for="iii">My-site : </label>
      <input type="text" name="iii" id='iii'>
      <input type="submit">
  </form>
```



### @@@@@@@action에 들어가는 목표 url 설정 주의사항@@@@@@@

```html
action="/catch/"
=> 127.0.0.1:8000/catch?name=asdf

action="catch/"
=> 127.0.0.1:8000/index/catch?name=asdf
```



1) throw.html - form action

2) /catch/로 요청

3) catch view - data로 받아서 처리함

4) catch.html 출력



#### /?~~~~ : Query string Parameters

request.GET.get()

: request 라는 장고 함수 선언할 때 넣어주었던 인자에 유저가 요청한 값이 들어 있음.



| 문자 | 설명                                                 | 예시           |
| ---- | ---------------------------------------------------- | -------------- |
| d    | 일 수에 대해서 2자리 숫자로 나타냅니다.              | 01~31          |
| j    | 일 수에 대해서 숫자로 나타냅니다.                    | 1~31           |
| S    | 일 수에 대해서 순서로 나타냅니다.                    | st, nd, rd, th |
|      |                                                      |                |
| m    | 월 수에 대해서 2자리 숫자로 나타냅니다.              | 01~12          |
| n    | 월 수에 대해서 숫자로 나타냅니다.                    | 1~12           |
| b    | 월 수에 대해서 영문 3자, 소문자로 나타냅니다.        | jan            |
| M    | 월 수에 대해서 영문 3자로 나타냅니다.                | Jan            |
| F    | 월 수에 대해서 영문으로 나타냅니다.                  | January        |
|      |                                                      |                |
| y    | 년도에 대해서 2자리 숫자로 나타냅니다.               | 19             |
| Y    | 년도에 대해서 4자리 숫자로 나타냅니다.               | 2019           |
|      |                                                      |                |
| D    | 요일에 대해서 3자리 문자로 나타냅니다.               | Fri            |
| I    | 요일에 대해서 문자로 나타냅니다.                     | Friday         |
|      |                                                      |                |
| G    | 시간에 대해서 24시 기준으로 나타냅니다.              | 0~23           |
| H    | 시간에 대해서 2자리 숫자로 24시 기준으로 나타냅니다. | 00~23          |
| g    | 시간에 대해서 12시 기준으로 나타냅니다.              | 1~12           |
| h    | 시간에 대해서 2자리 숫자로 12시 기준으로 나타냅니다. | 01~12          |
| a    | 시간에 대해서 오후, 오전을 소문자로 나타냅니다.      | a.m. , p.m.    |
| A    | 시간에 대해서 오후, 오전을 대문자로 나타냅니다.      | AM, PM         |
|      |                                                      |                |
| i    | 분에 대하여 2자리 숫자로 나타냅니다.                 | 00~59          |
|      |                                                      |                |
| s    | 초에 대하여 2자리 숫자로 나타냅니다.                 | 00~59          |