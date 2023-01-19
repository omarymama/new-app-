import streamlit as st
import numpy as np
from scipy.optimize import minimize

# 関数の定義
def func(x):
    return (x[0] - 3)**2 + (x[1] - 2)**2

# 関数の最小値を求める
result = minimize(func, [5, 5])

# StreamlitのUIを作成
st.title('最適化アプリ')

# 入力部分
st.write('最適化したい関数を入力してください')
st.write('例: (x[0] - 3)**2 + (x[1] - 2)**2')
user_input = st.text_input('関数:', '(x[0] - 3)**2 + (x[1] - 2)**2')

# 計算ボタン
if st.button('計算する'):
    try:
        # 関数を評価
        func = eval(f'def func(x): return {user_input}')
        exec(func)

        # 関数の最小値を求める
        result = minimize(func, [5, 5])
        
        # 結果を表示
        st.write('最適解:')
        st.write(result.x)
        st.write('最小値:')
        st.write(result.fun)
    except:
        st.write('入力された関数が正しくありません')
