# CSS layout

: 웹 페이지에 포함되는 요소들을 취합하고 어느 위치에 놓일지 제어하는 기술



## Float

: 웹페이지의 특성 요소를 띄우는 것. 

float된 이미지 좌 우측 주변으로`텍스트를 둘러싸는 레이아웃`을 위해 도입

더 나아가 이미지가 아닌 다른 요소들에도 적용해 웹 사이트의 전체 레이아웃을 만드는데까지 발전.





### Float 속성

기본값 : none

좌 : 좌에 띄어짐

우: 우에 띄어짐





# Flexbox (CSS Flexible Box Layout)

* 요소 간 공간 배분과 정렬 기능을 위한 1차원 레이아웃



* 요소

  * flex container (부모요소)
  * flex item (자식 요소)

* 축

  * main axis(메인축)

  * cross axis(교차축)

    

    ### flexbox의 시작

  ```html
  .flex-container {
    display: flex;
  }
  ```

  

### flex에 적용되는 속성

* 배치 방향 설정
  * flex-direction
* 메인축 방향 정렬
  * justify-content
* 교차축 방향 정렬
  * align-items, align-self(교차축 기준 선택한 요소 하나 정렬), align-content
* 기타
  * flex-wrap( 겹치는 부분은 아래로 떨어뜨림) , flex-flow, flex-grow, order



### content & items & self

* jusify-content
  * flex-start, flex-end, center, space-between, space-around, space-evenly
* align-items
  * flex-start, flex-end, center, stretch, baseline
* align-content
  * flex-start, flex-end, center, stretch, space-between, space-around
* align-self
  * auto, flex-start, flex-end, center, baseline, stretch



### inline-flex

: 자기가 가진 컨탠츠 만큼만 flex됨.

```html
.flex-container {
  display: inline-flex;
  flex-direction: row;
}
```



