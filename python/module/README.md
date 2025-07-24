## 모듈 과 제어문

### 모듈
한 파일로 묶인 변수와 함수 모음

내장 모듈 사용하기
- import 문
    같은 이름의 함수가 여러 모듈에 있을 때 충돌을 방지할 수 있다
    ```
    import math

    def pi():
        return 

    math.pi()
    math.sqrt
    ```

- from 절 사용
    코드가 짧고 간결해짐
    정의된 모듈의 위치를 알기 어려울 수 있음
    같은 이름의 함수가 겹치게 되면 동작이 이루어지지 않을 수 있음
    *모든 요소를 한 번에 import 하는 * 표기는 권장하지 않음*

    ```
    from math import * # xx
    from math import pi

    def pi():
        return
    # 겹침
    
    ```

    as 키워드를 사용하여 별칭을 부여할 수 있음
    import 되는 함수나 변수명이 너무 길거나, 자주 사용해야할 경우 별칭을 정의해 쉽게 사용할 수 있음


직접 다른 파일에 모듈을 정의하여 사용할 수 있음
from (폴더명) import (파일(모듈)명)

## 패키지
연관된 모듈을 하나의 디렉토리에 모아 놓은 것
- 모듈들의 이름 공간을 구분하여 충돌을 방지해줌
- 모듈들을 효율적으로 관리

> 다양한 패키지들을 포함하는 상위 개념을 라이브러리라고 한다. 
라이브러리 > 패키지 > 모듈 

- 내부 패키지
    - math, os, sys, random, copy 등 다양한 패키지가 존재한다
        - sys : 코드로 컴퓨터를 제어하는데 사용
        - os : 파일 구조 (폴더 구조) - 경로 조작 ..
        - 내장 함수 help를 통해 모듈에 무엇이 들어있는지 확인 가능함 
        `help(math)`

- 외부 패키지
    - 필요한 기능을 사용하기 위해 직접 설치해서 쓰는 패키지
    - 설치할 때 pip를 사용한다 `pip install requests`
    - https://pypi.org/  -  외부 패키지 설치할 수 있고, 등록 후 배포도 할 수 있다.

### requests 패키지
파이썬에서 웹에 요청을 보내고 응답받기를 쉽게 해준다
- 위치 설정을 따로 안 해도 global 환경에 저장된다

주로 사용하는 메서드
.get(URL) : 주어진 url로 요청한다
.json() : 돌아온 답을 json 자료형으로 변경해준다


## 제어문
코드의 실행 흐름을 제어하는데 사용되는 구문
조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행한다

### 조건문
if (조건):
    실행내용
>if , elif , else
조건에는 반드시 표현식을 사용해야한다. 
표현식이란? 결과가 값으로 평가되는 코드 (T/F)

* 조건식을 동시에 검사하는 것이 아니라 순차적으로 비교한다.

### 반복문
iterable한 객체의 요소들을 반복하는데 주로 사용

* iterable
: 반복 가능한 객체 , 즉 차례대로 접근하거나, 순회할 수 있는 객체들
- 리스트, 튜플, 문자열, 딕셔너리, 집합 등

- for문 
> for (변수) in (반복 가능 객체 )
> for index(idx/i .. ), fruit in enumerate(fruits):

주로 반복 횟수가 정해진 경우에 사용한다


- while 
조건이 참인 동안 반복
반복 횟수가 정해지지 않은 경우 주로 사용한다

break : 남은 코드 무시하고 반복 종료
continue : 다음 코드는 무시하고 반복문 처음으로 돌아가 다음 반복 수행
pass : 아무 동작 하지 않음


### map 함수
map(function, iterable)
```
numbers = [1, 2, 3]
result = map(str, numbers)

# 활용
nums = input().split()
print(nums) #['1', '2', '3']

nums2 = list(map(input().split()))
print(nums) #[1, 2, 3]
```

### zip함수
여러개의 반복 가능한 데이터 구조를 묶어서 같은 위치에 있는 값들을 하나의 tuple로 만든 뒤 zip으로 반환

```
girls = ['jenny','hi']
boys = ['jack','jay']
pair = list(zip(girls, boys))

# [('jane', 'jack'), ('hi','jay')]


# 활용
scores = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
]

for score in zip(*scores):
    print(score)

'''
(1,1,1)
(2,2,2)
(3,3,3)
'''
```
