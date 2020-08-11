# HTML (Hyper Text Markup Language)

* 웹 페이지를 작성하기 위한 언어, 웹 컨텐츠의 의미와 구조를 정의

* html의 구조

  ```html
  <!DOCTYPE html>     #html 문서 정의
  <html>
      <head>      #해당 html 문서의 정보를 담고 있다. / 브라우저에는 나타나지 않음. / (제목, 문자의 인코딩, 외부 로딩 파일 지정)
          
      </head>
      <body>		#브라우저 화면에 실질적으로 나타나는 정보
          
      </body>
  </html>
  ```

  

  * DOM tree: 부모, 형제 관계

  * 요소(element): 태그와 컨텐츠로 구성

    * 태그 별로 속성이 있는데 사용하는 속성은 다르다.

    * 시멘틱 태그: 의미론적 요소를 담은 태그

      * 개발자 및 사용자 뿐만 아니라 검색엔진 등의 의미 있는 정보의 그룹으로 표현 가능.

      

    * 그룹 컨텐츠: 

      * p: 문단을 구분 지을 때,   hr: 윗쪽과 아래쪽 그룹을 나누고 싶을 때, ol / ul / li : 리스트로 구성을 나누고 싶을 때, 

        pre,        blockquote: 인용구를 넣을 수 있음,     div: 구분을 짓는 태그

        

    * 텍스트 관련: 

      * a: 링크를  걺 , b: 굵게 , i: 기울기 , strong: 굵게, em, 기우리기, span: 내용 추가, br: 줄바꿈, img: 이미지 삽입

        

    * 테이블 관련:

      * tr, td: 테이블 set, th: 테이블 제목,    thead: tr,td,th를 묶음,     tbody, tfoot, caption:테이블에 제목이나 설명 넣을 수 있음

        

    * form 태그: 서버에 처리될 데이터를 제공하는 역할

      * input: 다양한 타입을 가지는 입력 데이터 필드
        * 공통 속성: name,   placeholder: text 칸이 어떤 데이터를 받아야 하는지 안내, required: 해당 입력은 필수,       autofocus: 커서가 고정되게 함
        * type: text, radio (동그라미), checkbox, date, password..
        * label 태그: 서식 입력 요소의 캡션





# CSS (Cascading Style Sheets)

* CSS: 스타일, 레이아웃 등을 통해서 문서를 표시하는 방법을 지정하는 언어

* CSS 적용 방법

  

  * inline: 태그 안에다가 직접 적용  / 수정하려면 일일이 다 찾아서 수정해야함 -> 관리하기 힘듦 -> test용

    * ```css
      <div style="background-color: red;"></div>
      ```

    

  * 내부 참조 방식: 하나의 html에서만 적용. -> 공부, test 용

    * ```css
      <style> h1 { color: red; } </style>
      ```

    

  * 외부 참조 방식: CSS정의를 파일 단위로 묶어서 필요한 html 문서마다 적용이 가능 / 유지보수 쉬움 / but 파일을 따로 만들어서 관리 해야함

  

* CSS 정의 하는 방법

```html
선택자 {
	속성: 속성값;
	속성2: 속성속성;
}
```



* 선택자: 특정한 요소를 선택하여서 스타일링을 하기 위해 반드시 필요함.

  * 기초 선택자

    * 타입(요소, 태그) 선택자
    * id 선택자: 해당 html 문서상 하나만 존재해야함.
    * 클래스 선택자: 여러군데 같은 이름으로 선언 가능
    * 전체 선택자: 문서 전체에 대한 내용을 설정 가능

  * 고급 선택자

    * 자손 선택자: 하위의 모든 요소 (띄워쓰기로 구분)

      ```css
      선택자1 선택자2 {속성: 속성값}           article p{color: red;}         # 태그 두 개가 한 칸 띄어진 형태
      ```

    * 직계 자손 선택자: 바로 아래의 요소만,  (>로 구분)

      ```css
      선택자1 > 선택자2 {속성: 속성값}         div > p{color: blue;}
      ```

    * 형제 요소 선택자: 같은 레벨에 있는 요소 (~로 구분)      / 멀리 있더라도 같은 레벨에 있다면 가능

      ```css
      선택자1 ~ 선택자2 {속성: 속성값}         p ~ section {color: yellow;}
      ```

    * 인접 형제 요소 선택자: 바로 붙어 있는 형제 요소를 선택 (+로 구분)

      ```css
      선택자1 + 선택자2 {속성: 속성값}         div + p{color: purple;}
      ```

      

* CSS 적용 우선순위

  

  1. 중요도:  !important로 나타냄 / 디버깅이 어려울 수 있으므로 사용시 주의

     

  2. 각 선택자 마다의 우선순위

     1) inline: 태그에 직접 스타일을 적용한 것

     2) id 선택자

     3) 클래스 선택자

     > *4) 속성 선택자*
     >
     > 	* 설렉테[속성]: 해당 속성을 가진 요소를 선택
     > 	* 셀렉터[속성=속성값]: 해당 속성을 가진 요소를 선택
     >
     > *5) 수도 클래스 선택자*
     >
     > ​	* 셀렉터:hove : 해당 셀렉터 위에 마우스를 오버했을 때 해당 셀렉터가 선택되서 바뀜.

     6) 요소 (타입, 태그)선택자

     : 범용(*)선택자, ('',+,~,>) 결합자는 우선 순위에 영향을 미치지 않음.

     

  3. 코드에 정의된 순서

  

* CSS 단위
  * px, % (부모로 부터 받은 비율 중에서 몇 % 비율로 공간을 차지하는지), em(부모로부터 받은 값의 계수만큼), rem(root 사이즈에서 배수)
  * vw(뷰포트 너비의 1%), vh, vmin(뷰포트에서 가로,세로 중에서 가장 짧은 쪽의 1%), vmax (뷰포트에서 가로,세로 중에서 가장 긴 쪽의 1%)
  * Hex(#), rgb, hsl(색조, 체도, 명도), rgba, hsla (투명도)
* Box Model
  * margin: 바깥 여백
  * border: 테두리
  * paddling: 안쪽 여백
  * content: 글이나 이미지등의 실제 요소
  * box-sizing
    * content-box: default 값 -> 콘텐츠 영역의 크기
    * border-box: 박스 모델 테두리 기준으로 크기 조절
* margin 상쇄
  * 수직 간의 형제 요소에서 주로 발생
  * margin 대신 paddling을 이용하여 안쪽부터 여백을 줌으로써 해결

* CSS Display
  * block: 하나의 블록으로 영역을 차지
    * div, ul, ol, li, p, hr, form 
  * inline
    * span, a, img, input, label, b, em, i, strong
    * 컨텐트의 너비 만큼 공간을 차지
    * width, height, margin-top, margin-bottom은 지정할 수 없음.
  * inline-block
    * 컨텐츠 너비 만큼 공간을 차지
    * width, height, maring-top, margin-bottom을 지정할 수 있음.
  * none: 공간을 없애 버림.
    * visibility: hidden 은 공간은 차지 but 화면에 표시 x
* CSS Position
  * static: 기본적인 배치 순서에 따름 (기본값)
  * relative: 자기 자신의 초반 위치를 기준으로 이동 (자리를 남겨둔 채 이동)
  * absolute: static 속성이 아닌, 가장 가까운 부모 / 조상 요소를 기준으로 이동
    * 기본적인 배치 순서에서 제외됨. (자리를 아에 빼버리고 이동)
  * fixed: 부모 요소와 관계 없이 브라우저를 기준으로 이동
  * sticky: relative 처럼 기본 배치 순서는 가지고 있음.
    * 화면 밖으로 벗어나면 fixed 처럼 위치에 고정되어 있음.
    * 부모의 영역이 화면 밖으로 벗어나면 다시 일반적인 흐름을 따름.