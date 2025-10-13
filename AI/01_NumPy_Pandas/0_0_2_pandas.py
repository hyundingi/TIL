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
# print(df)

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
