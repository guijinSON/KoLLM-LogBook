import streamlit as st
import pandas as pd
import numpy as np
import streamlit_scrollable_textbox as stx
import streamlit.components.v1 as components
  
st.set_page_config(layout="wide")

st.title('KoLLM-LogBook 📘')

def compare_models():
    df = pd.read_csv("Ko_LLM_LogBook.csv")

    prompt = st.selectbox('프롬프트를 선택해주세요.',(df.Question.values))


    col1, col2, col3 = st.columns(3)

    with col1:
        model1 = st.selectbox('비교할 모델을 선택해주세요.',
                              (list(df.columns[3:])),
                              index=0, key = 1)

        model1_output = df[df["Question"]==prompt][model1].values[0]
        stx.scrollableTextbox(model1_output, height=800, key = 11)

    with col2:
        model2 = st.selectbox('비교할 모델을 선택해주세요.',
                              (list(df.columns[3:])),
                              index=1, key = 2)

        model2_output = df[df["Question"]==prompt][model2].values[0]
        stx.scrollableTextbox(model2_output, height=800,  key = 21)

    with col3:
        model3 = st.selectbox('비교할 모델을 선택해주세요.',
                              (list(df.columns[3:])),
                              index=2,key = 3)

        model3_output = df[df["Question"]==prompt][model3].values[0]
        stx.scrollableTextbox(model3_output, height=800,  key = 31)
        
def amphora_small_instruct_report():
    
    with open("reports/amphora-small-instruct.html", "r") as file:
        html_content = file.read()
    components.html(html_content,
                    height=2000,
                   scrolling=True )
    
def kyujinpy_KoR_Orca_Platypus_13B_report():
    
    with open("reports/kyujinpy-KoR-Orca-Platypus-13B.html", "r") as file:
        html_content = file.read()
    components.html(html_content,
                    height=2000,
                   scrolling=True )
    
def krevas_LDCC_Instruct_Llama_2_ko_13B_v4_report():
    
    with open("reports/krevas-LDCC-Instruct-Llama-2-ko-13B-v4.html", "r") as file:
        html_content = file.read()
    components.html(html_content,
                    height=2000,
                   scrolling=True )
    
def gpt_3_5_turbo_0613_report():
    
    with open("reports/gpt-3.5-turbo-0613.html", "r") as file:
        html_content = file.read()
    components.html(html_content,
                    height=2000,
                   scrolling=True )

    
page_names_to_funcs = {
    "Compare Models": compare_models,
    "[Report] amphora/small-instruct": amphora_small_instruct_report,
    "[Report] kyujinpy/KoR-Orca-Platypus-13B": kyujinpy_KoR_Orca_Platypus_13B_report,
    "[Report] krevas-LDCC-Instruct-Llama-2-ko-13B-v4": krevas_LDCC_Instruct_Llama_2_ko_13B_v4_report,
    "[Report] gpt-3.5-turbo-0613": gpt_3_5_turbo_0613_report

}

demo_name = st.sidebar.selectbox("Choose a Report", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()