# database.py

# 파이썬
# - sqliet3
#   컴퓨터가 종료되도 데이터가 남아있다. (DB)
# - 데이터베이스
# Data 자료
# Base 기반

# 이름들 =[]

# print("시작하고 나서 이름들:", 이름들)
# 이름 = input("이름을 입력하세요?")

# 이름들.append(이름)

# print("입력 후 이름들:",이름들)

# 프로그램이 종료되면 그안에 있는 내용들이 싹다 사라지는 문제를 database가 저장
# 파일을 실행하면 도구들을 가져온다.
# 여러 사람과 함께 쓸수 있도록 데이터를 정리해서 영구적인 곳!
# - 실시간으로 데이터 수정도 가능하고 삭제도 추가도 마음대로 할 수 있도록 만든 프로그램

# 데이터베이스를 관리해주는 프로그램(DBMS)

import sqlite3 as db    #저장소
import streamlit as st  #웹 화면

# 데이터베이스 저장할 수 있는 공간 만들기

con = db.connect("검색어.db")       #폴더옆에 파일 생김ㄷㄷ

# 데이터베이스 공간을 조작할 수있는 커서
조작 = con.cursor()

# 데이터를 저장하려면 어떤 기록을 저장할지 미리 알려줘야된다.
# 테이블(표 형식)
# 사용하는 키워드(명령어)
# create table 테이블명
#   -첫번째 실행을 할 때 이미 디비한테 테이블 만듬
조작.execute("""
    create table if not exists searchlist(
        msg text 
    )

""")


# 네이버,구글에서 검색한 기록을 저장하는 프로그램
검색어목록 =[]

st.title("검색어 저장하는 DB보기")
st.write()

# 입력창에 입력을 하다 보면 앞뒤로 공백이 생길 수 있다.
# 아예 입력받을 때 공백을 제거하는 기능(아이디나 패스워드를 받을때!)
검색어 = st.text_input("검색어").strip()

# 버튼을 눌렀을 때 검색어를 searchlist 테이블에
# 저장
# insert into 테이블명 values 값 (파이썬에서 append 같은...)

# 검색이라는 버튼을 눌렀을때 비어있는 값은 저장 안함
# 출력 

# 파이썬은 if 변수가 만나게 되면 값이 있따면 True 없다면 False
if st.button("검색"):
    if 검색어: #검색어가 비어있지 않다면!
        조작.execute(f"""
            insert into searchlist
            values ('{검색어}')
    """)
        st.success(f"{검색어}저장 완료!")

        # 한번 더 저장(지워지지 않게 저장)
        con.commit()
    else:
        st.warning("검색어를 입력하세요!!!")
# 데이터베이스에 저장하고 수정하고 제일 마지막에는 데이터베이스를 닫아야됨
con.close()

# st.write("시작하고 검색어목록보기")
# st.write(검색어목록)


# if st.button("검색"):
#     검색어목록.append(검색어)

# st.write("끝나고 검색어목록보기")
# st.write(검색어목록)  #streamlit은 웹화면에 한번 띄운 순간 위에서 아래로 다시 실행이 되기떄문에 데이터가 계속 비어있음.

# --------------------------------------------------------------------------------------------------------------------
# import sqlite3 as db
# import streamlit as st

# con = db.connect("검색어.db")
# 조작 = con.cursor()

# 조작.execute("""
#     create table if not exists searchlist(
#     msg text
#     )
# """)
# ///////////
# 검색어목록 =[]
# st.title("검색어 저장하는 DB보기")
# st.write()
# 검색어 = st.text_input("검색어").strip()
# if st.button("검색"):
#   if 검색어:
#       조작.execute(f"""
#           insert into searchlist(
#            values('{검색어}'))
#    """)
#        st.success(f"{검색어}저장 완료!")
#        con.commit()
#   else:
#       st.warning("검색어를 입력하세요.")
# con.close()






















