import streamlit as st
st.title("택시 요금(새 요금표)")

km_당요금 = 1000
기본요금 = 4800
거리 = st.number_input("거리를 입력:",min_value=0,value=1)


요금 = 거리 * km_당요금 + 기본요금
st.write(f"[거리 {거리} 입력] 요금: {요금} 원")
st.write(f"검산: {km_당요금} x {거리} + {기본요금} = {요금}")


