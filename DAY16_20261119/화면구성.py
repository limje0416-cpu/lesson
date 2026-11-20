# assignment.py
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Machine Learning Prediction", layout="centered")

# ---------- 스타일 ----------
st.markdown(
    """
    <style>
    .badge {
        float: right; padding: 2px 10px; border-radius: 12px;
        background: #0f3d1f; color: #3ddc84; font-size: 12px;
    }
    .sub { font-size: 13px; color: #cfcfcf; margin-bottom: 4px; }
    .big { font-size: 22px; font-weight: 700; margin-top: -6px; }
    .info-label { font-size: 12px; margin-bottom: 0; }
    .info-value { font-size: 16px; font-weight: 700; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- 데이터 ----------
def show_preview(df: pd.DataFrame):
    """상위 n행 + 말줄임(---) 행을 우측 정렬 테이블로 표시"""
    df = df.style.hide(axis="index")
    st.write(df)

def 힌트_평가(df, target, hints, base_mae, base_mse):
    X = df[hints]
    y = target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    predict = model.predict(X_test)

    mae = mean_absolute_error(y_test, predict)
    mse = mean_squared_error(y_test, predict)

    mae_diff = base_mae - mae
    mse_diff = base_mse - mse

    return {
        "hints": hints,
        "intercept": model.intercept_,
        "coef": model.coef_,
        "mae": mae,
        "mse": mse,
        "mae_diff": mae_diff,
        "mse_diff": mse_diff,
        "predictResult": predict,
    }


# 데이터 소스 (CSV 업로드가 없으면 샘플 데이터 사용)
uploaded = st.sidebar.file_uploader("CSV 업로드 (선택)", type="csv")
df = pd.read_csv(uploaded) if uploaded else pd.DataFrame({})
total_rows, total_cols = df.shape

# ---------- 헤더 ----------
st.title("Machine Learning Prediction")
st.caption("데이터 기반 머신러닝 학습 및 예측 시스템")
st.divider()

# ---------- 01. 전체 데이터 확인 ----------
st.subheader("01. 전체 데이터 확인")
st.markdown(
    f'<span class="sub">전체 데이터 미리보기</span>'
    f'<span class="badge">{total_rows:,} rows</span>',
    unsafe_allow_html=True,
)

show_preview(df)
st.caption(f"전체 데이터 {total_rows:,}행 / {total_cols}개 컬럼")
st.divider()

# ---------- 02. 학습 데이터 범위 지정 ----------
st.subheader("02. 학습 데이터 범위 지정")

c1, c2 = st.columns(2)
with c1:
    train_start_row = st.number_input("학습 시작 행", value=1, min_value=1, max_value=max(df.shape[0], 1))
with c2:
    train_end_row = st.number_input("학습 종료 행", value=1, min_value=1, max_value=max(df.shape[0], 1))

if train_start_row > train_end_row:
    st.error("시작 행은 종료 행보다 클 수 없습니다.")
    st.stop()

train_df = df.iloc[train_start_row - 1 : train_end_row]

st.markdown(
    f'<p class="info-label">선택된 학습 데이터</p>'
    f'<p class="info-value">{len(train_df):,}행 / {train_df.shape[1]}개 컬럼</p>',
    unsafe_allow_html=True,
)

st.markdown('<p class="sub">학습 데이터 미리보기</p>', unsafe_allow_html=True)
show_preview(train_df)
st.divider()

# ---------- 03. 예측 데이터 범위 지정 ----------
st.subheader("03. 예측 데이터 범위 지정")

c1, c2 = st.columns(2)
with c1:
    test_start_row = st.number_input("예측 시작 행", value=1, min_value=1, max_value=max(df.shape[0], 1))
with c2:
    test_end_row = st.number_input("예측 종료 행", value=1, min_value=1, max_value=max(df.shape[0], 1))

if test_start_row > test_end_row:
    st.error("시작 행은 종료 행보다 클 수 없습니다.")
    st.stop()

test_df = df.iloc[test_start_row - 1 : test_end_row]

st.markdown(
    f'<p class="info-label">선택된 학습 데이터</p>'
    f'<p class="info-value">{len(test_df):,}행 / {test_df.shape[1]}개 컬럼</p>',
    unsafe_allow_html=True,
)

st.markdown('<p class="sub">학습 데이터 미리보기</p>', unsafe_allow_html=True)
show_preview(test_df)
st.divider()

# ---------- 04. 머신러닝 학습 및 예측 시작 ----------
st.subheader("04. 머신러닝 학습 및 예측")

st.session_state["trained"] = False

if st.button("🚀 AI 학습 및 예측 시작", type="primary", use_container_width=True):
    answer = df["방문자수"]

    single_data = [
        ["장서수"],
        ["도서예산"],
        ["장서수","사서수"],
        ["사서수"],
    ]

    data_set = [
        ["장서수","사서수"],
        ["장서수","도서예산"],
        ["사서수","도서예산"],
        ["장서수","사서수","도서예산"]
    ]

    X_base, X_test_base, y_train_base, y_test_base = train_test_split(
        df[["장서수", "사서수", "도서예산"]], answer, test_size=0.2, random_state=1
    )
    visitor_num = y_train_base.mean()
    baseline = [visitor_num]*len(y_test_base)

    base_mae = mean_absolute_error(y_test_base,baseline)
    base_mse = mean_squared_error(y_test_base,baseline)

    for hint in single_data:
        result = 힌트_평가(df,answer,hint,base_mae,base_mse)

        st.write(
            f"{hint} - 기본값:{round(result['intercept'], 1)}, \n"
            f"기울기:{round(result['coef'][0], 2)}, \n"
            f"MAE:{result['mae']:.0f} (개선: {result['mae_diff']:+.0f}), \n"
            f"MSE:{result['mse']:.0f} (개선: {result['mse_diff']:+.0f})")

        st.markdown(
            f'<p class="info-label">예측 결과</p>',
            unsafe_allow_html=True,
        )
        st.write(result["predictResult"])

st.divider()