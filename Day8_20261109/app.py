# app.py


# Streamlit
# - 파이썬으로 웹사이트나 웹 애플리케이션을 쉽게
#   만들수있게 도와주는 도구!

# 설치
# pip install streamlit
#설치 확인
# streamlit --version

# python -m streamlit --version

# AI -> 머신러닝 기초

#1. 현재 파일이 실행될때 import 도구명
# 현재 streamlit 도구 안에 있는 기능들을 내가
# 다 사용하겠음! 
# as 줄임말
import streamlit as st

st.title("AI 리터러시 수업!")
st.header("Ai란?")
st.write("컴퓨터가 사람의 지능적인 작업을 수행하도록 만드는 기술!")

#웹사이트에 그림이나 이미지 올때 사용하는 기능!
# image("파일명.확장자") 
st.image("1_ai.png")

#2. 위에 내용을  실행!
# 내 컴퓨터 안에서만 볼 수 있는 웹사이트 실행!
# streamlit run 파일명.py
# 터미널 - cmd -> python -m streamlit run app.py
# 항상 코드를 작성하고 나면! 꼭! 저장하기
# ctrl + s

# 원하는 위치에 이미지 넣어주기!
# st스트림릿 부탁
# image 넣어주기!
st.image("1-1_rule.png")

st.header("규칙 기반 AI란?")
st.write("Rule-Based AI")
st.write("사람이 정한 규칙을 따른는 인공지능")

# 머신러닝
st.header("머신러닝(Machine Learning)")
st.write("데이터에서 규칙이나 패턴을 학습하는 기술")
st.write("사람이 모든 규칙을 직접 작성하지 않고 컴퓨터 데이터를 보고 패턴을 찾는다.")

# 머신러닝 이미지
st.image("2_ml.png")
# 파이썬 streamlit에 대해서 검색해보기!
# 생성형 Ai / LLM / 토큰 / 프롬포트 /컨텍스트 윈도우
# 생성형 Ai- 생성형 AI는 딥러닝 기반의 인공신경망을 활용하며, 특히 거대언어모델(LLM), 확산 모델(Diffusion Models), 트랜스포머(Transformer) 구조 등이 핵심 기술로 사용됩니다

# python -m streamlit run app.py

st.header("딥러닝(Deep Learning")
st.write("복잡한 데이터에서도 특징과 패턴을 학습할 수있는 기술")
st.write("얼굴인식,음성인식,제품불량 이미지 판별,의료 영상 분석지원")
st.write("여러 층의 인공신경망을 이용하는 머신러닝 기술")
st.image("3_dl.png")

# 생성형 AI란?
# 소제목
st.header("생성형 AI란?")
# 글작성
st.write("학습한 패턴을 바탕으로 새로운 결과물을 생성한다")
st.write("gpt로 글쓰기 , AI 그림 만들기")
# 이미지
st.image("4_genai.png")

# LLM란?
st.header("LLM?")
st.write("LLM은 딥 러닝(Deep Learning) 기술을 기반으로, " \
"어마어마한 양의 글(텍스트 데이터)을 미리 학습하여 인간처럼 자연스럽게 언어를 이해하고 문장을 만들어내는 인공지능입니다.")
st.image("5_llm.png")

# 프롬프트란?
st.header("prompt?")
st.write("AI에게 작업을 지시하거나 질문을 전달하는 입력 문장 전체를 의미합니다.")
st.image("6_prompt.png")

# 토큰이란?
st.header("token?")
st.write("디지털 환경에서 특정 정보, 권리, 자산, 또는 최소 단위를 나타내는 개념으로, 분야에 따라 의미와 활용 방식이 달라집니다.")
st.image("7_token.png")

# 콘텍스트란?
st.header("context?")
st.write("사용자의 쿼리를 이해하고 적절한 응답을 생성하기 위해 참고하는 모든 정보와 배경을 의미합니다.")
st.image("8_context.png")

# 할루시네이션이란?
st.header("hallucination?")
st.write("AI가 거짓이거나 오해를 부르는 정보를 사실처럼 내놓는 현상을 의미합니다.")
st.image("9_hallucination.png")

# 컷오프란?
st.header("cutoff?")
st.write("특정 기준에 미달한 대상이나 후보를 사전에 탈락시키거나 제외하는 절차를 의미합니다.")
st.image("10_cutoff.png")