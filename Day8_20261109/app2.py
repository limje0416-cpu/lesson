#app2.py
# python -m streamlit run app2.py

# 1. app2파일을 실행할때 스트림릿(웹사이트)
#  도구를 포함해줘!
import streamlit as st

# 2.대주제를 작성함
st.title("단어 퀴즈")

# 3. 퀴즈1
st.header("문제1")
st.write("사람이 정한 규칙에 따라 작동하는 AI는?")

# 4.정답 입력받기
정답1 = st.text_input("1번 정답 입력")

# 5. 입력한 글 화면에 보이기!
#  입력받은 값을 정답1 변수에 넣고 화면에 보여줘! write()
st.write(정답1)

# 6.입력받은 정답1하고 비교해서 맞으면 정답입니다!
#                           틀리면 다시 도전하세요!
if 정답1 == "규칙 기반AI":
    st.write("정답입니다!")
elif 정답1 =="":
    st.write("")
else:
    st.write("다시 도전하세요!")

# 저장 후 브라우저 가서 F5 새로고침해서 결과 확인

st.header("문제2")
st.write("데이터에서 패턴을 학습하는 기술?")

#1. 입력받기
정답2 = st.text_input("2번 정답을 입력")  #오류가 났다 입력탭에서 어떤 입력을 가져와야하는지 헷갈리기 떄문에!
# 2.정답은 머신러닝
# 맞으면 정답입니다
# 다시 도전하세요!
if 정답2 == "머신러닝":
    st.success("정답입니다.")
elif 정답2 == "":
    st.write("")
else:
    st.error("다시 도전하세요!")

#  python -m streamlit run app2.py  
# 입력을 받고 나서 데이터가 있니 없니?
# 입력 받은 문자 안에서 공백을 제거하는 기능! (함수)
if 정답1 != "":
    if 정답1 == "머신러닝":
        st.write("정답")
    else:
        st.write("다시")

# ""false 
# "한문자" true

 