# Web 이란?

: 웹 어플리케이션 개발을 위해서. 





# HTML (Hyper Text Markup Language)

: 웹 컨텐츠의 의미와 `구조를 정의`하는 언어



  ### *mark-up : text에 의미를 부여하는 것.

### *markup language: 

태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

단순하게 데이터를 표현만 함.

ex) HTML, Markdown





## HTML 기본 구조



### head 요소

: 문서 제목, 문자코드(인코딩)과 같이 해당 문서 정보를 담고 있으며 브라우저에 나타나지 x

css 선언 혹은 외부 로딩 파일 지정 등도 작성.



### body 요소

브라우저 화면에 나타나는 정보로 실제 내용에 해당



## DOM(Documnet Object Model) 트리



* Documnet

  * <html>

    * <head>

      * `<title> - text: "My title"`

    * <body>

      * Element: <h1> - text: "A heading"
      * Element<a>  - attribute: href
        * text: "Link text"



### 요소 (element)

: <h1>contents</h1>

 HTML의 요소는 태그와 내용으로 구성되어 있다.



### 속성(attributes)

: <a href="http://google.com"></a>

​	속성명 (공백 x)              속성값(" "사용!)





### HTML Global Attribute

: 모든 html 요소가 공통으로 사용할 수 있는 속성

* id, class
* hidden
* lang
* style
* tabindex
* title



## 시멘틱 태그

* HTML5에서 `의미론적 요소`를 담은 태그



* 장점

  1) 읽기가 쉬워진다.

  ​	* 개발자가 의도한 요소의 의미가 명확히 드러남.

  ​	* 코드의 가독성을 높이고 유지보수를 쉽게 함.

  2) 접근성이 좋아진다.

  	* 검색엔진 -> 시각장애용 스크린리더 -> 더 나은 사용자 경험 제공.



* 대표적인 태그들

  * header: 문서 전체나 섹션의 헤더 (머릿말)
  * nav: 내비게이션
  * aside: 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  * section: 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  * article: 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  * footer: 문서 전체나 섹션의 푸터(마지막 부분)

  



### 그룹 컨텐츠

* `<p>`

  :**HTML `<p>` 요소**는 하나의 문단을 나타냅니다. 

* `<hr>`

  : 가로줄

* `<ol>, <ul>`

  : **HTML `<ol>` 요소**는 정렬된 목록을 나타냅니다. 보통 숫자 목록으로 표현합니다.

    **HTML `<ul>` 요소**는 정렬되지 않은 목록을 나타냅니다. 보통 불릿으로 표현합니다.

* `<pre>`

  : 우리가 만든 그대로를 보여줌 / 10칸 띄우면 10칸 띄워짐

* `<blockquote>`

  :인용문

* `<div>`

  : **HTML `<div>` 요소**는 플로우 콘텐츠를 위한 통용 컨테이너입니다. [CSS](https://developer.mozilla.org/ko/docs/Glossary/CSS)로 꾸미기 전에는 콘텐츠나 레이아웃에 어떤 영향도 주지 않습니다.



## 텍스트 관련 요소

`<a>: 하이퍼링크 걸어줌`

`<b> : 단순 bold처리`

`<strong>: bold처리 + 시멘틱태그 (의미적인 요소가 담겨져 있음)`

`<i>: itelic 체`

`<em>: itelic + 의미` 



`<span>`

 : HTML `<span>` 요소**는 구문 콘텐츠를 위한 통용 인라인 컨테이너로, 본질적으로는 아무것도 나타내지 않습니다. 스타일을 적용하기 위해서, 또는 `lang` 등 어떤 특성의 값을 서로 공유하는 요소를 묶을 때 사용할 수 있습니다. 적절한 의미를 가진 다른 요소가 없을 때에만 사용해야 합니다. `<span>`은 [``](https://developer.mozilla.org/ko/docs/Web/HTML/Element/div)와 매우 유사하지만, [``](https://developer.mozilla.org/ko/docs/Web/HTML/Element/div)는 [블록 레벨 요소](https://developer.mozilla.org/ko/docs/Web/HTML/Block-level_elements)인 반면 `<span>`은 [인라인 요소](https://developer.mozilla.org/ko/docs/Web/HTML/Inline_elements)입니다.



`<br>: 줄바꾸기`

`<img>: 이미지 삽입`



## table

`<tr>: table row : 테이블 한 열을 묶을 때`

`<td> : cell 안에 들어가는 데이터를 나타낼 때`

`<th>: table header : 각 열마다 데이터를 나타낼 때`

`<thead>: <th></> 들의 묶음`

`<tbody>: `**HTML** **`<tbody>`** 요소는 표의 여러 행()을 묶어서 표 본문을 구성합니다.

`<caption>: 테이블 제목`

`<colspan>: 열 단위로 셀 병함(좌, 우로 넓어짐)`

`<rowspan>: 행 단위로 셀 병합(위, 아래로 넓어짐)`

`<scope>: 해당 head에 scope가 있으면 어떠한 방향으로 영향력 있는지 나타냄`

`<col>: 열 방향으로 영향력 / <colgroup>으로 묶을 수 있음`

`<row>: 행 방향으로 영향력 / <rowgroup>으로 묶을 수 있음`



## @@@@@@@@@ Form @@@@@@@@@

* `<form>`은 서버에서 처리될 데이터를 제공하는 역할
* `<form>`의 기본 속성
  * action : 데이터를 보내는 목적지를 적는 곳
  * method



```html
<body>
  <h1>Throw 페이지</h1>
  <form action="/catch/" method="GET">
      <label for="name">데이터 입력 : </label>
      <input type="text" id='name' name="name">
      <label for="iii">My-site : </label>
      <input type="text" name="iii" id='iii'>
      <input type="submit">
  </form>
</body>
```



## input

* 다양한 타입을 가지는 입력 데이터 필드
* `<label>` : 서식 입력 요소의 캡션
* `<input>` 공통 속성
  * name, placeholder
  * required
  * autofocus



# CSS (Cascading Style Sheets)

## CSS 구문

```html
h1 {
	color: blue;
	font-size: 15px;
}
```



## CSS 정의 방법

## `사용자에게 문서를 표시하는 방법을 지정하는 언어.`



### 1. 인라인

태그 안에다가 직접 작성 (style)



### 2. 내부 참조

`<head> 안에 <style> 안에다가 작성`



### 3. 외부 참조

CSS를 단독 파일로 빼버림. <link>로 작성

-> 공통되는 것들을 외부 참조로 빼버려서 필요할 때마다 가져다 쓰면서 반복 감소, 효율성 높임.





# CSS Selector

### 선택자 (selector)

* HTML 문서에서 특정한 요소를 선택하여 스타일링 하기 위해서는 반드시 선택자라는 개념 필요.



* 기초 선택자
  * 전체 선택자, 타입 선택자
  * 클래스 선택자, 아이디, 속성 선택자
* 고급 선택자
  * 자식., 자손 선택자
  * 형제, 인접형제 선택자
* 의사 클래스 (pesudo class)
  * 링크, 동적 의사 클래스
  * 구조적 의사 클래스





id선택자 는 문서상에서 한번만 사용할 수 있다.   #red { }

class는 반복 가능.      // `클래스선택자가 두개면 마지막에 정의된 클래스를 따른다.`

전체선택자는 앞에 *{ }

자식선택자: 바로 아래에 선택자 가능. (두 단계는 안됨.)

자손선택자: 모두.

태그선택자: p {}  / h2 {}      등등...





`#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(1) > a`

NM_FAVORITE안에                                     class 두개                                   li안에 첫번째 자식안에 a까지



## @@@@@@@@CSS 적용 우선순위@@@@@@@@

1) !important

2) 인라인 / id / class / 요소(태그)

3) 소스 순서





### CSS 상속

: CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.

* 되는 것: TEXT 관련 요소 (font, color, text-align), visibility, opacity



* 안되는 것: bod-model 관련 / position 관련



### CSS 단위

* px
* %
* em : 배수 단위, 상대적인 사이즈를 가짐 (부모에 적용된 사이즈 기준)
* rem: html의 사이즈를 기준으로 배수 단위를 가짐
* viewport 기준 단위



## CSS Box Model

* Margin: 테드리 바깥 외부여백
* Border: 테두리 영역        /     .border{ 2px solid black;}
* padding: 테드리 안쪽의 내부 여백
* content: 글이나 이미지 등 요소의 실제 내용



## Box Model 구성 (margin/ padding)

1) 상하좌우 

: `.margin-1{margin: 10px;}`



2) 상하/좌우

: `.margin-2{margin: 10px 20px;}`



3) 상/ 좌우 / 하

:`.margin-3{margin: 10px 20px 30px;}`



4) 상 우 하 좌

:`.margin-4{margin: 10px 20px 30px 40px;}`



## Box-sizing

* 기본적으로 모든 요소의 box-sizing은 content-box
  * padding을 제외한 순수 contents 영역만을 box로 지정
  * 
* border까지의 너비를 하려면 -> `border-box` 로 지정



## Margin collapsing (마진 상쇄)



## CSS display

: 모든 요소는 네모이고, 어떻게 보여지는지에 따라 문서에서의 배치가 달라진다.



* ### display: block

  * 줄 바꿈이 일어나는 요소

  * 화면 크기 전체의 가로폭 차지

  * 블록 레벨 요소 안에 인라인 레벨 요소 들어갈 수 o

    

* ### display: inline

  * 줄 바꿈 일어나지 x
  * content 너비만큼 가로폭 차지
  * width height margin-top, bottom 지정 x
  * 상하 여백은 line-height로 지정

*  ### 대표적인 블록 레벨 요소

  *  div   /  ul ol li / p  / hr / form

  

* ### 대표적인 인라인 레벨 요소

  * span / a / img / input, label / b, em , i ,strong



## 속성에 따른 수평 정렬

* ### block은 margin



* ### text는 text-align





## CSS Position

: 문서상에서 요소를 배치하는 방법



* relative: static 위치를 기준으로 이동 (상대 위치)  / 원래 공간 안비움

* absoulte: 가장 가까이 있는 부모 조상 요소를 기준으로 이동 (절대 위치)  / 원래 공간 비움

* fixed: 부모 요소와 관계 없이 브라우저를 기준으로 이동 (고정위치)

  -> 스크롤시에도 항상 같은 곳에 위치