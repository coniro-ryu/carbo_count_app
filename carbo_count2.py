import math

import streamlit as st

st.title("簡易カーボカウント")

# --- dict ---
time_dict = {"朝": 30, "昼": 30, "夜": 40}
food_dict = {
    "米": {"weight": 160, "ratio": 0.4},
    "パン": {"weight": 160, "ratio": 0.5},
    "麺": {"weight": 160, "ratio": 0.2},
}
side_dict = {"油なし": 10, "油あり": 20}

# --- 糖質比 ---
st.subheader("糖質比")
time = st.radio(
    "時間帯を選んでください", list(time_dict.keys()), index=0, horizontal=True
)
time_val = st.number_input(f"糖質比({time})", value=time_dict[time])

# --- 食事 ---
st.subheader("食事")
food = st.radio("主食", list(food_dict.keys()), index=0, horizontal=True)
side = st.radio("副食", list(side_dict.keys()), index=0, horizontal=True)

food_val = st.number_input(food, value=food_dict[food]["ratio"])
side_val = 10 if side == "油なし" else 20

# --- 設定値 ---
st.subheader("設定値")
target = st.number_input("目標血糖値", value=100)
isf = st.number_input("インスリン効果値", value=150)
premeal = st.number_input("食前血糖値", value=0)

S = food_val + side_val
A = S / food_val
B = (premeal - target) / isf
total = A + B
total_trunc = math.floor(total * 100) / 100

st.markdown("### 結果")
st.markdown(
    f"""
    <div style='font-size:22px; line-height:2'>
        <strong>糖質量(g)：</strong> <span style='color:green; font-size:30px'><strong>{S:.0f}</strong></span><br>
        <strong>注入量(U)：</strong> <span style='color:blue; font-size:30px'><strong>{total_trunc:.2f}</strong></span>
    </div>
    """,
    unsafe_allow_html=True,
)
