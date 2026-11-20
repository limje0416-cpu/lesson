import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

영수증 = pd.DataFrame({
    "곡수": [1,2,3],
    "요금(원)":[500,1000,1500]
})

X = 영수증[["곡수"]]
Y = 영수증["요금(원)"]

model = LinearRegression()

model.fit(X,Y)

st.write(f"1곡당 요금은(기울기):{round(model.coef_[0])}")
st.write(f"기본 요금:{round(model.intercept_)}")

예측 = model.predict(pd.DataFrame({"곡수":[8]}))[0]

st.write(f"8곡 예측:{예측:,.0f}원")

