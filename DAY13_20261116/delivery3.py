import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("컴퓨터가 요금표를 찾는다.")

영수증 = pd.DataFrame({
    "개수":[1,2,3],
    "총액":[13000,22000,31000]
})

X = 영수증 [["개수"]]
Y = 영수증["총액"]

model = LinearRegression()

model.fit(X,Y)

st.write(f"메뉴 1개당 가격(기울기):{round(model.coef_[0])}")
st.write(f"배달비(절편):{round(model.intercept_)}")

개수 = st.number_input("몇 개 시킬까요?",value=5,min_value=1)

예측 = model.predict(pd.DataFrame({"개수":[개수]}))[0]
st.write(f"예측 총액({개수}개수): {예측:,.0f}원")
