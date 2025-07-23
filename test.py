def create_user(name, age):
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age

    print(f'{name}님 환영합니다!')
    return user_info

name = ['홍길동', '이순신', '유관순']
age = [30, 20, 50]

result = list(map(create_user, name, age))
print(result)