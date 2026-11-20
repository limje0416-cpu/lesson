import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("재료가 2개인 배달 요금")

배달 = pd.DataFrame({
    "개수":[1,2,3,2,1],
    "거리":[1,2,1,3,2],
    "총액":[14500,27000,38500,27500,15000]
})

X = 배달[["개수","거리"]]
Y = 배달["총액"]

st.write(f"X 크기:{X.shape}")

model = LinearRegression()
model.fit(X,Y)

st.write(f"기울기:개수 {round(model.coef_[0])},거리{round(model.coef_[1])}")
st.write(f"절편:{round(model.intercept_)}")

예측 = model.predict(pd.DataFrame({"개수":[4],"거리":[4]}))[0]
st.write(f"4개, 4km 예측:{예측:,.0f}원")
