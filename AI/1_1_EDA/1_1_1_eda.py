import pandas as pd
import numpy as np
from sklearn.datasets import load_wine

# [선형 회귀 ]

df, y = load_wine(as_frame=True, return_X_y=True)
df['quality'] = y
df.info()
print(df.describe())

# pandas 연습
# 1. 데이터셋에 포함된 와인의 총 샘플 수 구하기
# print(df.shape)
sample_count = df.shape[0]
print('샘플 수 : ', sample_count)

# 2. 데이터셋의 특성 수 구하기
feature_count = df.shape[1]
print('특성 수 : ', feature_count)

# print(df.head())

# 3. quality는 어떤 범주가 있는지 구하기
class_count = df['quality'].nunique()
print('클래스 수 : ', class_count)

# 4. quality 별 샘플 수 구하기(0, 1, 2가 각각 몇 개 인지?)
class_distribution = df['quality'].value_counts().sort_index()
print('클래스 별 샘플 갯수 : ', class_distribution)

# 5. Alcohol의 평균값이 가장 높은 클래스를 구하기
top_alcohol_class = df.groupby('quality')['alcohol'].mean().idxmax()
print('알코올 함량이 높은 quality : ', top_alcohol_class)

# 8. color intensity가 10 이상인 샘플의 비율
# 필터 진행 - series 형태
filtered_df = df['color_intensity'] >= 10
# 원본에서 시리즈가 True인 애들만 뽑아서 샘플 생성
high_color_samples = df[filtered_df]
# 전체에서 해당 갯수의 비율 구하기
high_color_ratio = len(high_color_samples) / len(df) * 100
print('high color ratio : ', high_color_ratio)

# 10. Proline의 분포에서 가장 높은 피크를 가지는 클래스 번호 구하기
# 히스토그램 
import matplotlib.pyplot as plt
df['proline'].hist(by=df['quality'], figsize=(10, 10), edgecolor='black', color='lightblue')
plt.suptitle('proline Distribution by class')
# plt.show()

# 몇 개 단위로 데이터를 끊을지
bins = 20
global_min, global_max = df['proline'].min(), df['proline'].max()
peak_by_class = {}

for cls in df['quality'].unique():
    counts, _ = np.histogram(df.loc[df['quality'] == cls, 'proline'], bins=bins, range=(global_min, global_max))
    peak_by_class[int(cls)] = counts.max()

print(peak_by_class)

# 12.alcohol과 상관관계가 가장 높은 특성 구하기
# 상관관계란 
alcohol_correlations = df.corr()['alcohol']
alcohol_correlations = alcohol_correlations.abs().sort_values(ascending=False)
print(alcohol_correlations)
top_corr_with_alcohol = alcohol_correlations.index[1]
print(top_corr_with_alcohol)
pro_al_corr = df['proline'].corr(df['alcohol'])
print(pro_al_corr)




# 전체 상관관계 시각화
# 모든 상관관계 저장
corr = df.corr()

fig, ax = plt.subplots()
n = len(corr)
mask = np.triu(np.ones((n, n)))

import seaborn as sns
sns.heatmap(data=corr, annot=True, fmt='.2f', cmap='coolwarm', mask=mask)
ax.grid(False)
ax.set_title('Correlation between features')

#flavanoid 분포
plt.figure(figsize=(6,4))
sns.histplot(data=df, x='flavanoids', bins=20, kde=True)
plt.title('Flavanoid Distribution')
plt.show()


# 산점도 그리기
sns.scatterplot(data=df, x='flavanoids', y='total_phenols', hue='quality')
plt.show()


# 결측치와 이상치

# 결측치 탐지

# -1. 난수 고정
np.random.seed(42)

# 0. 결측치 생성
df_missing = df.copy()
missing_idx = np.random.choice(df_missing.index, size=10, replace=False)
df_missing.loc[missing_idx, 'flavonoids'] = np.nan # 숫자가 아님을 의미 (= 데이터가 존재하지 않는다, 결측치)

# heatmap으로 결측치 확인
sns.heatmap(df_missing.isnull(), cbar=False)
plt.title('visualize missing values')
plt.show()


# 이상치 탐지

# 0. 이상치 생성
outlier_idx = np.random.choice(df_missing.index, size=5, replace=False)
df_missing.loc[outlier_idx, 'alcohol'] = df_missing['alcohol'].mean() * 5

# 4분위 범위(IQR)로 이상치 탐지
# 전체 데이터를 구간별로 4등분 해서 가운데 두 구간의 크기를 IQR로 정의할 때,
# 첫번째 구간(제일 작은 구간) - IQR * 1.5
# 세번째 구간의 최솟값 + IQR * 1.5
# 를 벗어나는 데이터를 이상치로 판단

def detect_outliers_iqr(data, column):
    # data = df
    # column = ['alcohol']
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[column] < lower_bound | (data[column]) > upper_bound)]

outliers_alcohol = detect_outliers_iqr(df_missing, 'alcohol')

# boxplot으로 이상치 확인
sns.boxplot(x=df_missing['alcohol'])
plt.title('alcohol putliers')
plt.show()

# 결측치는 평균값으로 대체
df_filled = df_missing.fillna(df_missing.mean(numeric_only=True))
print(df_filled.isnull().sum())

# 이상치 처리
# 1. 이상치 제거
df_no_outliers = df_filled[~df_filled.index.isin(outliers_alcohol.index)]
outliers_alcohol = detect_outliers_iqr(df_no_outliers, 'alcohol')
print(outliers_alcohol) # 이상치가 제거된 것을 확인할 수 있다.

# 2. 평균값으로 대체 (이상치들을)
mean_alcohol = df_filled['alcohol'].mean()
df_filled.loc[outliers_alcohol.index, 'alcohol'] = mean_alcohol
outliers_alcohol = detect_outliers_iqr(df_filled, 'alcohol')
print(outliers_alcohol)
