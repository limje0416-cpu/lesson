from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv("전국국립도서관통계.csv")
#데이터 항목: 평가년도,도서관구분,도서관코드,도서관명,행정구역,시군구,장서수,사서수,방문자수,도서예산

print(data.columns)
print(data[["장서수","사서수","도서예산"]].head(5))
print(data[["장서수","사서수","도서예산"]].isna().sum())

answer = data["방문자수"]

single_data = [
    ["장서수"],
    ["사서수"],
    ["도서예산"]
]

data_set = [
    ["장서수","사서수"],
    ["장서수","도서예산"],
    ["사서수","도서예산"],
    ["장서수","사서수","도서예산"]
]

#중복내용 함수화
def 힌트_평가(df, target, hints, base_mae, base_mse):
    X = df[hints]
    y = target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    predict = model.predict(X_test)

    mae = mean_absolute_error(y_test, predict)
    mse = mean_squared_error(y_test, predict)

    mae_diff = base_mae - mae
    mse_diff = base_mse - mse

    return {
        "hints": hints,
        "intercept": model.intercept_,
        "coef": model.coef_,
        "mae": mae,
        "mse": mse,
        "mae_diff": mae_diff,
        "mse_diff": mse_diff,
    }


#1-1.기준선(평균 예측) 계산
X_base, X_test_base, y_train_base, y_test_base = train_test_split(
    data[["장서수", "사서수", "도서예산"]], answer, test_size=0.2, random_state=1
)
visitor_num = y_train_base.mean()
baseline = [visitor_num]*len(y_test_base)

base_mae = mean_absolute_error(y_test_base,baseline)
base_mse = mean_squared_error(y_test_base,baseline)

print()
print(f"평균 방문자 수: {visitor_num:,.1f}명")
print(f"기준선 MAE: {base_mae:,.1f}명")
print(f"기준선 MSE: {base_mse:,.1f}명")
print()
#1-2. 각 항목별 단독 결과 + 기준선 대비 오차
for hint in single_data:
    result=힌트_평가(data,answer,hint,base_mae,base_mse)
    print(
        f"{hint} - 기본값:{round(result['intercept'], 1)}, "
        f"기울기:{round(result['coef'][0], 2)}, "
        f"MAE:{result['mae']:.0f} (개선: {result['mae_diff']:+.0f}), "
        f"MSE:{result['mse']:.0f} (개선: {result['mse_diff']:+.0f})")
print()
print()
#오차가 적은 순서: 사서수 > 도서예산 > 장서수
#----------------------------------------------
#2.다중회귀 조합
for hints in data_set:
    result = 힌트_평가(data, answer, hints, base_mae, base_mse)
    print(
        f"조합: {hints} - 기본값:{round(result['intercept'], 1)}, "
        f"MAE:{result['mae']:.0f} (개선: {result['mae_diff']:+.0f}), "
        f"MSE:{result['mse']:.0f} (개선: {result['mse_diff']:+.0f})")
    print()
    for name, w in zip(hints, result["coef"]):
        print(f"{name} 기울기: {round(w, 2)}")
print()
print()
#>>>>>>>> 어떤 조합도 [사서수]단독보다 유의미한 값이 없음