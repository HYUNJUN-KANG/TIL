# Bootstrap



### CSS를 reboot 하는 방법 2가지

* Reset: 브라우저 자체 스타일을 없애버림



* Nomalize (Bootstrap)

  : 웹 표준에 맞춤, 지키지 못하는 IE가 존재할 경우 나머지 브라우저를 IE에 맞춤.





### CDN (Content Delivery(Distribution) Network)

: 컨텐츠 (CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템.



### Spacing

#### .mt-1       # margin-top

```html
.my-1 {
  margin-top: 0.25rem !important;
}
```



| class name | rem  | px   |
| ---------- | ---- | ---- |
| m-1        | 0.25 | 4    |
| m-2        | 0.5  | 8    |
| m-3        | 1    | 16   |
| m-4        | 1.5  | 24   |
| m-5        | 3    | 48   |

* 1 rem = 16 px



#### .mx-0 : margin-left, right (가로란 의미) 가 0이다.

#### .mx-auto : 수평 중앙

#### .py-0: padding 상,하를 0으로



| t    | top         |
| ---- | ----------- |
| b    | bottom      |
| x    | left, right |
| y    | top, bottom |



# Responsive Web

하나의 코드를 구축해서 그걸 돌려 씀 -> `bootstrap의 grid system이용`



## Grid system

* bootstrap grid system은 flexbox로 제작

* container, rows, column으로 컨텐츠를 배치하고 정렬

  

  * ### 12개의 column

  * ### 5개의 grid breakpoints



```html
<div class="container">
    <div class="row">
        <div class="col"></div>
        <div class="col"></div>
        <div class="col"></div>
    </div>
</div>
```



### Grid system breakpoints

| .col-    | .col-sm- | .col-md | .col-lg- | .col-xl- |
| -------- | -------- | ------- | -------- | -------- |
| 576 미만 | 576 이상 | 768     | 992      | 1200     |

