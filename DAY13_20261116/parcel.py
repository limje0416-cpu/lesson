import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

표 = pd.DataFrame ({
    "무게" : [1,2,3,4],
    "요금" : [4000,5000,6000,7000]
})

X = 표[["무게"]]
Y = 표["요금"]

model = LinearRegression()

model.fit(X,Y)

st.write(f"1kg 당 요금(기울기):{round(model.coef_[0])}")
st.write(f"기본 운임(절편):{round(model.intercept_)}")

kg = st.number_input(" 몇 kg 일까요?",value=5,min_value=1)

예측 = model.predict(pd.DataFrame({
    "무게": [10]}))[0]

st.write(f"10kg 예측:{예측:,.0f}원")
