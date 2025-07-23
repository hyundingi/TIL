# 실습 문제 풀면서 막힌 거

## 2025-07-23
### 배열 속에 들어있는 지 확인하기
```
if user['blood_type] in blood_types: 
    # types 리스트에서 해당 유저가 갖고 있는 blood_type을 갖고 있는 지 확인하는 구문

if '@' in user['email]:
    # 유저의 이메일 안에 @이라는 문자가 있는 지 확인
    in 뒤에는 리스트 값이 들어와야함.
```

### 빈 리스트는 뭘까
```
arr = []
if arr:
    ()
else:
    ()
    # 파이썬은 빈 리스트를 False라고 생각해서 저런 구문이 있다면 else를 돌려준다..

print(arr is None) # False
print(arr == None) # False
print(not arr) # True
print(arr == []) # True
```
Type으로 따졌을 때 []는 <class 'list'> 를 출력하고
None 은 <class 'NoneType'> 를 출력한다. 

### 그거에 이어서 if 의 진릿값 ,, 그리고 return 
유효성 검사 함수를 만듬
모두 통과하면 True, 
하나라도 통과 못하면 False와 어떤 부분을 통과하지 못했는지 리스트에 담아 return 함.

```
# 문제의 if 문
if checked_user:
    user_list.append(i)
elif checked_user == 'blocked':
    worng_check += 1
else:
    worng_check += 1
    for worng in checked_user[1]:
        i[worng] = None
```

checked_user 에는 
True 혹은 (False, []) 였는데 `if checked_user:` 때문에 모든 return 값이 저기로 빠졌다 
