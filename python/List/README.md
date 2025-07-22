# PYTHON - List & 비교연산자 
| 불변 가변 / 얕은 복사 깊은 복사 / 단축평가

## 시퀀스 자료형
### 리스트 [ ]
- 여러개의 값을 순서대로 저장하고 변경 가능하다
- 인덱싱, 슬라이싱, 길이 확인, 반복 등 공통 기능 모두 사용 가능

> 인덱싱으로 값 수정하기 / 슬라이싱으로 여러 값 한번에 바꾸기
```
my_list = [1, 2, 3, 4, 5]

# 인덱싱으로 값 수정
my_list[1] = 'two'
print (my_list) # [1, 'two', 3, 4, 5]

# 슬라이싱으로 여러 값 한번에 바꾸기
my_list[2:4] = ['three', 'four']
print (my_list) # [1, 'two', 'three', 'four', 5]
```

### 튜플 ( )
- 여러개의 값을 순서대로 저장하지만 변경 불가
- 인덱싱, 슬라이싱, 길이 확인, 반복 등 공통 기능 모두 사용 가능
- 불변 특성을 사용하여 내부 동작과 안전한 데이터 전달에 사용됨

### range
- 연속된 정수 시퀀스를 생성하는 변경 불가 자료형
- 주로 반복문과 함께 사용됨 > 특정 횟수만큼 코드 반복 실행할 때 유용

**range(start,stop,step)**
**range(stop)** : 0 ~ stop-1
**range(start, stop)** : start ~ stop-1

*range는 list 형태로 변경 시 내부 값 확인이 가능함*

### 딕셔너리 { }
- key - value 쌍으로 이루어짐
- 순서와 중복이 없음(키값 한정)
- 변경 가능한 자료형
- 딕셔너리는 비시퀀스형 자료임! 

**키**
- 값을 식별하기 위한 고유한 이름표 (절대 중복 불가)
- 변경 불가능한 자료형만 키값이 될 수 있음
    - str, int, float, tuple
    - list , dict은 불가함

**값**
- 키에 해당하는 실제 데이터

```
for key in information:
    print(key, " : ", information[key]) # 따옴표 안 들어감
```

### 세트 { }
- 순서 없음
- 중복이 없음 .!!
- 변경 가능

딕셔너리와의 차이점 
: 키 - 밸류가 없음
: 생성할 시, `my_set = set()` 이렇게 만들어야함. (딕셔너리랑 혼동 주의)

```
my_set = {1, 2, 3}
my_set2 = {3, 6, 9}

# 합집합
print(my_set | my_set2) # {1, 2, 3, 6, 9}

# 차집합
print(my_set - my_set2) # {1, 2}

# 교집합
print(my_set & my_set2) #{3}
```

| 컬렉션명 | 변경 가능 여부 | 순서 존재 여부 |
| --- | --- | --- |
| str | X | O |
| list | O | O |
| tuple | X | O |
| dict | O | X |
| set | O | X |


### 불변(Immutable) vs 가변(Mutable)
```
my_str = 'hello'
my_str[0] = 'z'
# TypeError == str은 변경 불가

my_list = [1, 2, 3]
my_list[0] = 100
# [100, 2, 3] list형은 변경 가능
```

**얕은 복사**
- 객체를 새로운 변수로 복사하지만, 기존 객체의 주소값을 복사해옴
    - 원본값 훼손 가능성이 있음
    - a = b 이런식으로 나타냄

**깊은 복사**
- 객체 자체를 그대로 복사
    - a = b.copy() 함수 사용해서 나타냄


### 형변환
- 한 데이터 타입을 다른 데이터 타입으로 변환하는 과정
- 암시적 형변환 vs 명시적 형변환 
    - 암시적 : 연산 중에 자동으로 데이터 타입을 변환함
    ex) `print(3 + 5.0) # 8.0 으로 출력됨`
    - 명시적 : str(), int(), list() ,,, 등

### 비교 연산자
- == 연산자
값이 같은지를 비교함 (동등한지 비교)
```
print(2 == 2.0) # True
print(2 != 2) # False
print('HI' == 'hi') # False
print(1 == True) # True
```

- is 연산자
객체 자체가 같은 지 비교 (식별)
두 변수가 완전히 동일한 객체를 가리키는지 (= 메모리 주소가 같은지)
```
print(1 is True) # False
print(2 is 2.0) # False
```

**is 대신 ==을 사용해야 하는 이유**
- is는 정체성, ==은 가치를 비교함
- 두 연산자는 같다를 확인하는 목적이 다름
- == 은 주로 값을 비교할 때 사용

**반대 경우 (is 연산자는 언제 사용하는가)**
- 싱글턴 객체를 비교할 때 사용
    - 싱글턴 객체란 ? 
        - None, True, False 와 같이 하나의 객체만 생성되어 재사용 되는 특별개체들

```
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b) # True 두 리스트의 값은 동일하다
print(a is b) # False 서로 다른 리스트 객체이다

b = a
print (a is b) # True (얕은 복사 - 주소값 복사 / 같은 객체를 가리키고 있음)

# None 타입 은 값이 없음을 표현하는 데이터 타입임 
# 0이나 ''와는 다름
arr = [] 
print(arr is None) #False 가 출력됨 
```

### 단축평가
- and 연산자
    - 하나라도 거짓이면 거짓
    - 처음 만나는 거짓 값을 바로 반환
    - 마지막까지 참이면 마지막 참값 반환

- or 연산자
    - 하나라도 참이면 바로 참
    - 처음 만나는 참을 바로 반환
    - 모든 값이 거짓이면 맨 마지막 거짓 값을 반환

```
item1 = '지도'
item2 = '나침반'
result = item1 and item2
print(result) # 마지막 참 값인 나침반 출력

item2 = ''
result item1 and item2
print(result) # 거짓 값 ''출력

item1 = ''
item2 = '나침반'
result = item1 and item2
print(result) # ''(거짓)을 보자마자 바로 ''출력
```

### 멤버십 연산자
```
word = 'hello'

print('h' in word) # True
print('h' not in word) # False
print('z' in word) # False
```

### 시퀀스형 연산자
```
# + 연결하는 기능
# * 반복 연산
print([1, 2] + ['a', 'b']) # [1, 2 'a', 'b']
print([1, 2] * 2) # [1, 2, 1, 2]
```