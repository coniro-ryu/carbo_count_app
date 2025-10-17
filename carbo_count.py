import math

import streamlit as st

st.title("簡易カーボカウント")

# --- 糖質比 ---
st.subheader("**糖質比**")
time = st.radio("時間帯を選んでください", ["朝", "昼", "夜"], horizontal=True)
if time == "朝":
    ratio = st.number_input("糖質比(朝)", value=30)
elif time == "昼":
    ratio = st.number_input("糖質比(昼)", value=40)
else:
    ratio = st.number_input("糖質比(夜)", value=40)
carb_ratio = ratio

# --- 食事 ---
st.subheader("食事")
food = st.radio("主食", ["米", "パン", "麺"], horizontal=True)
side = st.radio("副食", ["油なし", "油あり"], horizontal=True)

# --- 設定値 ---
st.subheader("**設定値**")
target = st.number_input("目標血糖値", value=100)
isf = st.number_input("インスリン効果値", value=150)
premeal = st.number_input("食前血糖値", value=000)

if food == "米":
    food_val = 160 * 0.4
elif food == "パン":
    food_val = 160 * 0.5
elif food == "麺":
    food_val = 160 * 0.2
else:
    food_val = 0

side_val = 10 if side == "油なし" else 20

A = (food_val + side_val) / carb_ratio
B = (premeal - target) / isf
total = A + B
total_trunc = math.floor(total * 100) / 100

st.markdown(
    f"### 結果：  <span style='color:blue'>{total_trunc:.2f} 単位</span>",
    unsafe_allow_html=True,
)
