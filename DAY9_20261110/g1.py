# import streamlit as st

# st.title("게임1. AI보다 정확하게 세기")
# st.write("AI에게 글자수를 물어보고, 파이썬으로 확인해보자")

# 정답1 = st.text_input("문장을 입력하세요.")
# st.write(정답1)

# 셀글자 = st.text_input("셀 글자를 입력하세요.")
# st.write(셀글자)

# 개수 = st.text_input("AI가 말한 개수를 입력하세요.")
# st.write(개수)

# if 정답1 == "" or 셀글자 == "" or 개수 == "":
#     st.info("AI한테 말할 것 입력하세요")
# else:
#     진짜정답 = str(정답1.count(셀글자))
#     st.write("정답 개수 : ", 진짜정답)
#     if 진짜정답 == 개수:
#         st.success("맞았습니다")
#     else:
#         st.error("틀렸습니다")
# python -m streamlit run g1.py
# -------------------------------------------------------------------------
# 직접해보기
import streamlit as st
st.title("게임1. AI보다 정확하게 세기")
st.write("AI에게 글자수를 물어보고,파이썬으로 확인해보자!")

문장 = st.text_input("문장을 입력하세요!")
st.write(문장)

셀글자 = st.text_input("셀 글자를 입력하세요.")
st.write(셀글자)

개수 = st.text_input("AI가 말한 개수를 입력하세요!")
st.write(개수)

진짜정답 = str(문장.count(셀글자))
st.write("파이썬이 센 개수 :",진짜정답)

if 문장 
