import streamlit as st
import pandas as pd
import numpy as np
import streamlit_scrollable_textbox as stx

  
st.set_page_config(layout="wide")

st.title('KoLLM-LogBook 📘')

df = pd.read_csv("Ko_LLM_LogBook.csv")

prompt = st.selectbox('프롬프트를 선택해주세요.',(df.Question.values))


col1, col2, col3 = st.columns(3)

with col1:
    model1 = st.selectbox('비교할 모델을 선택해주세요.',(list(df.columns[3:])),key = 1)
    model1_output = df[df["Question"]==prompt][model1].values[0]
    stx.scrollableTextbox(model1_output, height=800, key = 11)

with col2:
    model2 = st.selectbox('비교할 모델을 선택해주세요.',(list(df.columns[3:])),key = 2)
    model2_output = df[df["Question"]==prompt][model2].values[0]
    stx.scrollableTextbox(model2_output, height=800,  key = 21)

with col3:
    model3 = st.selectbox('비교할 모델을 선택해주세요.',(list(df.columns[3:])),key = 3)
    model3_output = df[df["Question"]==prompt][model3].values[0]
    stx.scrollableTextbox(model3_output, height=800,  key = 31)

