import streamlit as st
import time

st.title('streamlit入門')
st.write('subtitle')

'start!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Interation {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)
'done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

left_column,right_column = st.columns(2)
button = left_column.button('右からむに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')

