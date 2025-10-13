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