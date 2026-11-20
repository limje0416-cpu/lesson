import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

자료 = pd.read_csv("도서관자료.csv", encoding="utf-8-sig")
방문자수 = 자료["방문자수"]

# 앞의 17개로 학습하고, 마지막 7개로 확인
y_train = 방문자수[:17]
y_test = 방문자수[17:]

# 모델 1: 장서수
힌트1 = 자료[["장서수"]]
모델1 = LinearRegression()
모델1.fit(힌트1[:17], y_train)
예측1 = 모델1.predict(힌트1[17:])

# 모델 2: 장서수 + 사서수
힌트2 = 자료[["장서수", "사서수"]]
모델2 = LinearRegression()
모델2.fit(힌트2[:17], y_train)
예측2 = 모델2.predict(힌트2[17:])

# 모델 3: 장서수 + 사서수 + 도서예산
힌트3 = 자료[["장서수", "사서수", "도서예산"]]
모델3 = LinearRegression()
모델3.fit(힌트3[:17], y_train)
예측3 = 모델3.predict(힌트3[17:])

# 실제값과 예측값 비교
print("정답       장서수       장서수+사서수       세 가지 힌트")
for 정답, 답1, 답2, 답3 in zip(y_test, 예측1, 예측2, 예측3):
    print(round(정답), round(답1), round(답2), round(답3))

# 오차 비교
print()
print("장서수 MAE:",
      round(mean_absolute_error(y_test, 예측1), 1))
print("장서수+사서수 MAE:",
      round(mean_absolute_error(y_test, 예측2), 1))
print("세 가지 힌트 MAE:",
      round(mean_absolute_error(y_test, 예측3), 1))

print()
print("장서수 MSE:",
      round(mean_squared_error(y_test, 예측1), 1))
print("장서수+사서수 MSE:",
      round(mean_squared_error(y_test, 예측2), 1))
print("세 가지 힌트 MSE:",
      round(mean_squared_error(y_test, 예측3), 1))