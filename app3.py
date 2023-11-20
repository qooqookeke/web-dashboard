# 판다스의 데이터 불러오는 방법
# 판다스의 데이터프레임을 웹 화면으로 보여주는 방법

import streamlit as st
import pandas as pd

def main() :
    st.title('아이리스 꽃 데이터')
    
    df = pd.read_csv('./data/iris.csv') # ./ :현재폴더, ../ :상위폴더

    st.dataframe(df)

    num_of_species = df['species'].nunique()

    st.text('아이리스 꽃의 종류는 총 '+ str(num_of_species) +'가지 입니다.')
    # 숫자열과 문자열을 함께 표시할 수 없음
    # 숫자열을 문자열로 변경 후 표시 : str(변수)

if __name__ == '__main__':
    main()

