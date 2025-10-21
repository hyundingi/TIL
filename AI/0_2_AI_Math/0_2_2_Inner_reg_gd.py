import seaborn as sns
import numpy as np

df = sns.load_dataset('diamonds')
df.info()
# print(df.describe())


categorical_cols = df.select_dtypes(include=['category']).columns.tolist()
continuous_cols = df.select_dtypes(include=['number']).columns.tolist()
print(categorical_cols)
print(continuous_cols)

# print(df.head(5))

# 연속형 변수들만 뽑아서 저장한다.
x_raw = df[continuous_cols].values

# 해당 변수들의 평균만 구한다.
# axis
# 1 3 -> 2
# 2 4
# ^ 1.5
mu = x_raw.mean(axis=0)
# 해당 변수들의 표준편차를 구한다.
std = x_raw.std(axis=0)

# 표준 편차가 0이 될 경우 바꿔준다.
# 1. 1로 바꾼다
std = np.where(std == 0, 1.0, std)
# 2. 아무 작은 값으로 변경해서 영향이 없게끔 하거나
apsilon = 1e-8
std = np.where(std == 0, apsilon, std)

# 표준화된 x 값들을 구한다.
# 원래값 - 평균 / 표준편차
x_norm = (x_raw - mu) / std

print(x_norm)

import pandas as pd
# 정규방정식으로 세타 만들기
# 계산의 편의를 위해 x_norm -> DataFrame
x_df = pd.DataFrame(x_norm, columns=continuous_cols)

# feature 와 label의 분리
x = x_df.drop(labels='price', axis=1).values
y = x_df['price'].values

# 절편항을 추가
m, n = x_norm.shape
x_b = np.c_[np.ones((m, 1)), x_norm]


# theta
theta = np.zeros(n + 1)
# 학습률 : 현재 지점에서 어느정도 이동할지
alpha = 0.01
# 반복 횟수
iterations = 1000
# 비용 계산 결과 기록
loss_history = []

from tqdm import tqdm
# 정해진 iterations 만큼 반복
for i in tqdm(range(iterations)):
    # 현재 theta에 대한 예측값을 계산
    y_pred = (x_b @ theta).flatten()
    
    # 예측값에 대하여 MSE 계산
    error = y_pred - y
    mse = np.mean(error ** 2)
    loss_history.append(mse)

    # MSE를 바탕으로 경사를 계산
    gradient = (2/m) * x_b.T @ error

    # 경사를 바탕으로 theta를 갱신
    theta -= alpha * gradient

import matplotlib.pyplot as plt
print("최종 θ:", theta.flatten())
print("최종 MSE:", loss_history[-1])

plt.plot(loss_history)
plt.xlabel("Iteration", size="large")
plt.ylabel("Mean Squared Error", size="large")
plt.title("Loss Curve", size="large")
plt.show()
