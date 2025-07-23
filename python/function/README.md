# 함수 
: 함수를 사용하는 이유?
- 코드의 중복 방지
- 가독성, 유지보수성 향상

### 함수의 구조
```
def make_sum(num1, num2):
    # 이처럼 함수의 구조 설명을 해주는 것을 덕스트링 이라고 한다.
	""" 두 수를 받아 
	두 수의 합을 구하는 함수입니다.
	"""
	return num1 + num2 
```
만약 return 값이 없을 시, None이 반환된다.

## 매개변수와 인자
### 매개변수
함수를 정의할 때 함수가 받을 값을 나타내는 변수

### 인자
함수를 호출 할 때 전달하는 값

```
# 아래에서 활용된 num1 , num2는 매개변수이다.
def make_sum(num1, num2):
	return num1 + num2
	
a = 2
b = 3

result = make_sum(a, b) # a와 b는 인자이다.
print(result)
```

## 다양한 인자
1. 위치 인자
- 인자의 위치에 따라 전달되는 인자 
```
def greet(name, age):
    print(name, age, '입니다')

greet('홍길동', 30) # 홍길동 30 입니다
greet(25, '유관순') # 25 유관순 입니다.
```
인자의 위치에 따라 매개변수가 할당된다

2. 기본 인자
- 함수 정의에서 매개변수에 기본 값을 할당
```
def greet(name, age = 30):
    print(name, age, '입니다')

greet('홍길동')
```

3. 키워드 인자
- 인자의 이름과 함께 값을 전달하는 인자
```
def greet(name, age):
    print(name, age, '입니다')

greet(name = '홍길동', age = 30) # 홍길동 30 입니다
greet(age = 25, name = '유관순') # 유관순 25 입니다.
```
순서가 달라도 알아서 잘 들어간다
**키워드 인자와 위치 인자를 같이 넣어 호출할 경우*키워드 인자가 반드시 뒤로* 가야한다**
`greet(25, name = '이순신')`

4. 임의의 인자 목록
- 정해지지 않은 개수의 인자를 처리하는 인자
- 여러 개의 인자를 tuple로 저장함
```
def greet(*args):
    print(args) # ('홍길동', 30, '남')

greet('홍길동', 30, '남')
```

5. 임의의 키워드 인자 목록
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 여러개의 인자를 dict로 묶어서 처리함
```
def greet(**kwargs):
    print(kwargs) # {name:'홍길동', age:30, gender:'남'}

greet(name = '홍길동', age = 30, gender = '남')
```

함수 인자 권장 작성 순서
**위치 > 기본 > 가변 > 가변 키워드**
`def func(pos1, pos2, default_arg=’default’, *args, **kwargs): .. `

### !! 형태가 비슷해서 헷갈림 주의

: 기본 인자는 함수의 매개변수에 기본 값을 할당하는 것
: 키워드 인자는 호출 시에 이름과 함께 값을 전달하는 것


### 재귀함수
1개 이상의 종료 상황이 존재하고 수렴하도록 작성해야한다.
- 종료 조건을 명확히 해야한다
- 반복되는 호출이 종료 조건을 향하게 해야 한다.

------

# 파이썬의 범위 !! Scope
```
def func():
	num = 20
	print('local', num) #local 20 > 함수 내에서만 참조 가능
	
func()
print('global', num) # num을 찾지 못함
```

1. built-in scope
파이썬이 실행된 이후부터 영원히 유지 

2. global scope
모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지

3. local scope
함수가 호출될 때 생성되고 함수가 종료될 때까지 유지

**아래와 같은 순서로 찾아나감 (LEGB Rule)**

local (현재 작업 중인 범위) > 
Enclosed (지역 범위 한 단계 위) > 
Global (최상단) > 
built-in(모든 것을 담고 있음)

함수 내에서는 바깥 scope의 변수에 접근 가능하지만 수정은 할 수 없음

```
x = 'g'
y = 'g'

def outer_func():
	x = 'e'
	y = 'e'
	def inner_func(y):
		z = 'h'
		print(x, y, z) # eph  > enclosed 범위의 e의 값을 가져온
	
	inner_func('p')
	print(x, y) # ee
	
outer_func()
print(x, y) # gg
```

### global 키워드
```
num = 0 # 전역 변수

def increment():
	global num # 함수 안에서 사용한 num을 전역 변수로 선언
	num += 1 # 그래서 수정이 가능함
	
print(num) # x

# 매개변수에 글로벌 키워드 사용하는 것은 불가능
```

### 함수 이름 작성 규칙
- 소문자와 언더스코어를 사용한다 
- 동사로 시작하여 함수의 동작을 설명한다
- 약어 사용을 지양한다
    - calculate ~ (price, tax)    | good
    - calc ~   (p, t)  | bad
- 이름 만으로 무엇을 하는지 명확하게 표현하는 이름이어야 한다.
- T/F를 반환한다면 is 혹은 has로 시작하는 것을 추천
- 동사 + 명사 > save_user()
- 동사 + 형용사 + 명사 > caculate_total_price()
- get/set + 접두사 > get_username(), set_username()

## 함수는 단일 책임 원칙을 져야한다.
모든 객체는 하나의 명확한 목적과 책임만을 가져야한다.

1. 명확한 목적
    함수는 한 가지 작업만 수행
    함수 이름으로 목적을 명확히 표현
2. 책임 분리
    데이터 검증, 처리, 저장 등을 별도 함수로 분리 해야함
    각 함수는 독립적으로 동작 가능하도록 설계해야함
3. 유지보수성
    작은 단위의 함수로 나누어 관리
    코드 수정 시 영향 범위를 최소화

디버깅 - 디버그를 해결하는 과정이다 

### 패킹, 언패킹 응용
```
# 언패킹
def func(x, y, z):
	print(x, y, z)
	
name = ['alice', 'jane', 'peter']
func(*name) # alice jane peter

my_dict = {'x': 1, 'y': 2, 'z': 3}
func(**my_dict) # 1 2 3

# 패킹
def func2(**kwargs):
	print(kwargs)
	print(type(kwargs))
	
func2(a=1, b=2, c=3)
# {'a':1, 'b':2, 'c':3}

def func3(*args):
	print(args)
	print(type(args))
	
func3(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
```

함수 매개변수 값에 *를 넣으면 패킹
함수 호출 시 인자 값에 *를 넣으면 언패킹

# 람다 표현식 !!
:  보통 map 함수와 함게 쓰인다
익명 함수를 만드는 데 사용되는 표현식
한 줄로 간단히 함수를 정의할 수 있다.

```
numbers = [1, 2, 3]

def square(x):
    return x ** 2

squared1 = list(map(square, numbers))
print(squared1) # [1, 4, 9, 16, 25]

# 람다사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2) # [1, 4, 9, 16, 25]
```

정리하자면 lambda (매개변수) : return 값 

### ++ lambda 를 활용한 sort
```
numbers = [5, 9, 6, 7, 8]

sorted_numbers = sorted(numbers, key=lambda number:numbers[0])
numbers.sorted(key= lambda number:number)

# number = 매개변수를 number로 칭할게.
# numbers[0] / number 요소 자체를 기준으로 삼아 정렬
```


### map과 map & lambda
```
def create_user(name, age):
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age

    print(f'{name}님 환영합니다!')
    return user_info

name = ['홍길동', '이순신', '유관순']
age = [30, 20, 50]

result = list(map(create_user, name, age))
<!-- 홍길동님 환영합니다!
이순신님 환영합니다!
유관순님 환영합니다!
[{'name': '홍길동', 'age': 30}, {'name': '이순신', 'age': 20}, {'name': '유관순', 'age': 50}] -->
```

함수를 활용해 딕셔너리를 만들고 list로 묶는다
> 반복문 쓸 필요 없다 !


```
# lambda 안에 내가 만들고자 하는 유형의 괄호를 넣어야함 // 마지막은 데이터를 가져올 뭉치
info_list = list(map(lambda x: {"name":x['name], "age":x['age'], many_user}))
```

위에 함수 대신에 lambda를 활용해서 한 줄로 해결할 수도 있다.
