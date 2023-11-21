import streamlit as st
import pandas as pd

def run_eda_app() :
    st.subheader('EDA 화면')
    df = pd.read_csv('./data/iris.csv')
    st.dataframe(df)
    st.subheader('상관 계수')
    st.dataframe(df.corr(numeric_only=True))
    #상관계수, numeric_only=True 숫자로 되어있는 것만 상관계수 구하기