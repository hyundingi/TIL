## NumPy 와 Pandas의 기초 문법

학습 목표 : Numpy, Pandas 활용해보기

### NumPy

많은 수를 한 번에 다루기 위한 라이브러리 

### Pandas

AI
- ML : 머신 러닝 (수학 - 다차원 배열을 이루는 수학)
    - DL : 딥 러닝 ( 인공신경망)
        - LLM : 챗지피티, 제미나이 등  (인공 신경망을 미친듯이 키운 것들 ..)

프롬프트 엔지니어링
MCP
A2A

### 선형회귀….

선형대수학을 통해서 다차원 데이터를 다루는 방법을 찾는다 … 

ㄴ 이차원 데이터를 다루는 연구였음.

그래서 N차원 데이터를 효과적으로 다룰 수 있는 넘파이와 판다스를 활용 

### 실습 해보기

1. 가상환경 설정
2. `pip install numpy pandas matplotlib`

### NumPy

```python
import numpy as np

"""
기본 행렬 생성 및 연산
"""

arr = np.array([1, 2, 3, 4, 5])
print(arr)

a = np.array([[1, 2], [3, 4]])
print(a)

b = np.array([[4, 3], [2, 1]])
print(b)

print(a @ b)

# @ - 행렬 곱 연산 (두 개 이상의 행렬을 곱한다)
"""
[[ 8  5]
 [20 13]]
"""

# 다차원 배열 생성
arr_2d = np.array([[10, 20, 30], [40, 50, 60]])
print(arr_2d)

# 단위 행렬 (A * E = A)
# 정사각형의 모양을 가진 행렬이 만들어져야하기 때문에
x = np.eye(3)
print(x)
"""
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""

print(a @ np.eye(2))
print(np.eye(2) @ b)
"""
[[1. 2.]
 [3. 4.]]
[[4. 3.]
 [2. 1.]]
"""
```

```python
import numpy as np

# 행렬의 원소를 인덱스를 바탕으로 변경하기
x = np.eye(3)

# 행렬 조작
x[0, 2] = 9
print(x)

"""
[[1. 0. 9.]
 [0. 1. 0.]
 [0. 0. 1.]]
"""

print(type(x)) # <class 'numpy.ndarray'>
```

```python
"""
무작위 정수 만들기
"""
arr_ran = np.random.randint(low=50, high=101, size=5)
print(arr_ran)

"""
정규 분포 추출
"""
std_ran = np.random.randn(3, 3)
print(std_ran)

"""
연산 / 형변환
"""
id_3 = np.eye(3)
std_ran = np.random.randn(3, 3)
# 다양한 차원에 대한 곱 / 내적
z = np.dot(id_3, std_ran)
print(z)

# 각 원소의 형변환
id_bool = id_3.astype(bool)
print(id_bool)
id_int = id_3.astype(int)
print(id_int)
"""
[[ True False False]
 [False  True False]
 [False False  True]]
[[1 0 0]
 [0 1 0]
 [0 0 1]]
"""

# 상수 곱 (스칼라 배)
x_float = id_3 * 1.1
print(x_float)
```

```python
"""
벡터(일차원) 연습
"""
# 기본 벡터 생성
v = np.array([1, 2, 3])

# v를 반복 복제
v_repeated = np.tile(v, (3, 1))
print(v_repeated)
"""
[[1 2 3]
 [1 2 3]
 [1 2 3]]
"""

# 다차원 행렬을 평탄화
v_flattened = v_repeated.flatten()
print(v_flattened)
"""
[1 2 3 1 2 3 1 2 3]
"""
```

```python
import numpy as np

"""
벡터(일차원) 연습
"""
# 균등한 간격을 가지는 일정크기의 벡터를 생성
thetas = np.linspace(0, 2 * np.pi, 120)

# 각 원소에 삼각함수 적용
sin_thetas = np.sin(thetas)
print(sin_thetas)

"""
시각화 해보기
"""
import matplotlib.pyplot as plt
plt.plot(thetas, sin_thetas)
print(sin_thetas)

plt.plot(thetas)
```


### Pandas

```python
import pandas as pd

"""
DataFrame
"""

data = {
    'name' : ['Alex', 'Brad', 'Chad'],
    'age' : [25, 30, 35],
    'score' : [55.5, 90.3, 78.9],
}

df = pd.DataFrame(data)
print(df)
"""
   name  age  score
0  Alex   25   55.5
1  Brad   30   90.3
2  Chad   35   78.9
"""

# series  - DataFrame의 열 (column)
name_series = df['name']
print(name_series)

# record 접근
# iloc - index 기반 접근
print(df.iloc[0])
print(df.iloc[0, 0], df.iloc[0, 2])

# loc - 라벨로 찾음
print(df.loc[2, 'name'])

# 여러 열을 추출
print(df[['name', 'score']]) # type - pandas.core.frame.DataFrame
```

```python
# 정보 찾아보기
df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   name    3 non-null      object
 1   age     3 non-null      int64
 2   score   3 non-null      float64
dtypes: float64(1), int64(1), object(1)
memory usage: 204.0+ bytes
"""
print(df.describe())
"""
        age      score
count   3.0   3.000000
mean   30.0  74.900000
std     5.0  17.741477
min    25.0  55.500000
25%    27.5  67.200000
50%    30.0  78.900000
75%    32.5  84.600000
max    35.0  90.300000
"""
```

```python
print(df.shape) # (3, 3)
print(df.columns.tolist()) # ['name', 'age', 'score']
print(df.index) # RangeIndex(start=0, stop=3, step=1)

# 상위 두개만 가져오기 
print(df.head(2))
"""
   name  age  score
0  Alex   25   55.5
1  Brad   30   90.3
"""
```

```python
"""
집계기능
"""

print(df['score'].mean()) # 평균
print(df['age'].max()) # 최대값
print(df.sort_values(by='score')) # 정렬
```

```python
"""
다양한 타입의 데이터를 활용하여 DataFrame 만들기
"""

# 여러 딕셔너리에서 만들기 --------------------------------------
alex = {'Name': 'Alex', 'Age': 25, 'Score': 85.5}
brad = {'Name': 'Brad', 'Age': 30, 'Score': 90.3}
chad = {'Name': 'Chad', 'Age': 35, 'Score': 78.9}

# 각 딕셔너리가 레코드라고 생각하고 리스트로 만들어줌
df_from_dict = pd.DataFrame([alex, brad, chad])
print(df_from_dict)

# 여러 리스트에서 만들기 -----------------------------------------
alex = ['Alex', 25, 85.5]
brad = ['Brad', 30, 90.3]
chad = ['Chad', 35, 78.9]

# 딕셔너리 형태에서는 키값이 있어서 상관없는데 리스트 형태는 columns를 지정해줘야함
df_from_list = pd.DataFrame([alex, brad, chad], columns=['name', 'age', 'score'])
print(df_from_list)

# numpy array에서 만들기 --------------------------
import numpy as np
nums = np.array([
    [25, 85.5],
    [30, 90.3],
    [35, 78.9],
])
names = ['alex', 'brad', 'chad']

# 나이와 점수로 DataFrame 만들기
df_from_ndarr = pd.DataFrame(nums, columns=['age', 'score'])
print(df_from_ndarr)

# 0번에 이름 추가하기
df_from_ndarr.insert(0, 'name', names)
print(df_from_ndarr)

# 시리즈 형변환
df_from_ndarr['score'] = df_from_ndarr['score'].astype(int)
df_from_ndarr['age'] = df_from_ndarr['age'].astype(int)
print(df_from_ndarr)

```