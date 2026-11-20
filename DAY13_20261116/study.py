import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("공부 시간과 점수")

공부 = pd.DataFrame({
    "시간":[1,2,3,4,5],
    "점수" :[52,58,71,78,88]
})

X = 공부[["시간"]]
Y = 공부["점수"]

model = LinearRegression()
model.fit(X,Y)

st.write(f"기울기:{model.coef_[0]:.1f}")
st.write(f"절편:{model.intercept_:.1f}")

for 시간 in [3,6,10]:
    예측 = model.predict(pd.DataFrame({"시간":[시간]}))[0]
    st.write(f"{시간}시간 예측: {예측:.1f}점")
