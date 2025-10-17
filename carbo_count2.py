import math

import streamlit as st

st.title("糖質量(g)")

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

st.markdown("### 結果")
st.markdown(
    f"""
    <div style='font-size:22px; line-height:2'>
        <strong>糖質量(g)：</strong> <span style='color:green; font-size:30px'><strong>{food_val + side_val:.0f}</strong></span><br>
        <strong>インスリン量(U)：</strong> <span style='color:blue; font-size:30px'><strong>{A:.2f}</strong></span>
    </div>
    """,
    unsafe_allow_html=True,
)
