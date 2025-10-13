import seaborn as sns
import numpy as np

# 시각화 함수
def plot_prediction(y_true, y_pred):
    y_true = y_true.flatten()
    y_pred = y_pred.flatten()
    assert y_true.shape == y_pred.shape, f"Size mismatch between y_true and y_pred"
    import matplotlib.pyplot as plt
    fig, ax = plt.subplot(figsize=(6, 4))

    # 회귀선
    sns.scatterplot(x=y_true, y=y_pred,
                    alpha=0.5, label="Model Prediction", ax=ax)

    # 이상적인 예측선
    sns.lineplot(x=[y.min(), y.max()],
                 y=[y.min(), y.max()],
                 label="Ideal Regression", linestyle="--", color="red")

    ax.set_xlabel('Actual Price')
    ax.set_ylabel('Predicted Price')
    ax.set_title('Actual vs Predicted Price')
    fig.tight_layout()
    plt.show()


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

# 정규방정식 계산
XT_x = x_b.T @ x_b
XT_y = x_b.T @ y

# np.linalg.inv를 통해 세타 구하기
theta = np.linalg.inv(XT_x) @ XT_y


# 예측값 만들기
y_pred = x_b @ theta
# MSE 계산 - 쓰기 힘들다.-
mse = np.mean((y_pred - y) ** 2)
plot_prediction(y_true=y, y_pred=y_pred)

# 최소제곱법
theta_lstsq, _, _, _ = np.linalg.lstsq(x_b, y, rcond=None)
y_pred = x_b @ theta_lstsq
plot_prediction(y, y_pred)

# SVD
u, s, vt = np.linalg.svd(x_b, full_matrices=False)
# 의사 역행렬 구하기
s_plus = np.diag(1.0 / s)
# theta 계산
theta_svd = vt.T @ s_plus @ u.T @ y

y_pred = x_b @ theta_svd
plot_prediction(y, y_pred)