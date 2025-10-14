import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

df, y = load_wine(as_frame=True, return_X_y=True)

# [2진 분류]
# 로지스틱 회귀 - 싸이틱런에 있는 로지스틱 회귀 메소드를 활용함
# quality를 0과 0아님으로 구분하는 이진 분류를 진행한다.
y[y == 0] = 0
y[y != 0] = 1

# feature와 y를 합친다.
df['quality'] = y
label = df['quality'].value_counts().sort_index()
print(label)
X = df.drop('quality', axis=1).values

# 학습 / 테스트 데이터 나누기 - 보통 7:3 .. 8:2
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size = 0.3,
    random_state=42,
    stratify=y, # 한곳에 한쪽 클래스가 몰리지 않게끔 나눠줌 
    )



# 표준화 전처리
# 데이터의 스케일을 조정해서 모든 특성이 같은 주요도를 갖게끔
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# 이전에 mean 을 구하고 std 로 표준편차, x_norm .. 을 구하던 방법을
#  한 번에 해결할 수 있다.

# 데이터 기준으로 표준화를 진행하는지
# 1)
# scaler.fit(X)
# X = scaler.transform(X)
# 2) 한번에 가능
# X = scaler.fit_transform(X)

# 1. 훈련 데이터로부터 표준화에 필요한 통계값 계산
X_train_norm = scaler.fit_transform(X_train)

# 2. 테스트 데이터의 통계값을 기준으로 학습 데이터를 표준화
X_text_norm = scaler.transform(X_test)

print(X_train.mean(axis=0))
print(X_test.mean(axis=0))


# 로지스틱 회귀 모델 학습
from sklearn.linear_model import LogisticRegression

# 1. LogisticRegression 모델 선언
clf = LogisticRegression(max_iter=1000)

# 2. .fit으로 학습
clf.fit(X_train, y_train)

# 3. X_test로 예측값 생성
y_pred = clf.predict(X_test)
print(y_pred)

# 평가 -> y_pred와 y_test가 얼마나 일치하는가?
from sklearn.metrics import confusion_matrix, classification_report

# 혼동행렬로 정답 예측 결과 비교
print(confusion_matrix(y_test, y_pred))
print()
print(classification_report(y_test, y_pred))

from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

y_score = clf.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_score)
auc = roc_auc_score(y_test, y_score)

# ROC 곡선 시각화 (matplotlib 사용)
plt.plot(fpr, tpr, label=f'ROC-AUC = {auc:.3f}')
plt.plot([0, 1], [0, 1], linestyle='--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()

"""
clf = LogisticRegression(max_iter=1000)
clf = LogisticRegression(max_iter=100)
둘이 그래프가 다르게 나온다.
100이 정확도 1로 나옴

그래프로 보았을 때 100쪽이 더 완벽하게 되었다고
이게 무조건 좋은 파라미터라는 것은 아니다.
"""