import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

자료 = pd.read_csv("도서관자료.csv", encoding="utf-8-sig")

# 힌트와 정답
힌트 = 자료[["장서수", "사서수", "도서예산"]]
방문자수 = 자료["방문자수"]

# 앞의 17개로 학습하고, 마지막 7개로 확인
X_train = 힌트[:17]
y_train = 방문자수[:17]

X_test = 힌트[17:]
y_test = 방문자수[17:]

# 베이스라인: 앞의 방문자수 평균으로 예측
평균 = sum(y_train) / len(y_train)
기준선예측 = [평균] * len(y_test)

# 모델 학습 후 예측
모델 = LinearRegression()
모델.fit(X_train, y_train)
예측 = 모델.predict(X_test)

# 실제 방문자수와 두 예측을 한 줄씩 비교
print("정답       평균예측      모델예측")
for 정답, 평균답, 모델답 in zip(y_test, 기준선예측, 예측):
    print(
        round(정답),
        round(평균답),
        round(모델답)
    )

# 두 방법의 오차 비교
기준선MAE = mean_absolute_error(y_test, 기준선예측)
모델MAE = mean_absolute_error(y_test, 예측)

print()
print("베이스라인 MAE:", round(기준선MAE, 1))
print("모델 MAE:", round(모델MAE, 1))
print("베이스라인 MSE:", round(mean_squared_error(y_test, 기준선예측), 1))
print("모델 MSE:", round(mean_squared_error(y_test, 예측), 1))

print()
print("MAE가 줄어든 양:", round(기준선MAE - 모델MAE, 1))
print("계수:", 모델.coef_.round(2))
print("절편:", round(모델.intercept_, 2))