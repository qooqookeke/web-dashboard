import streamlit as st

from app_home import run_home_app
from app_eda import run_eda_app
from app_ml import run_ml_app

# 파일 분리해서 개발하는 방법

def main():
    st.title('파일 분리 앱')

    menu = ['홈','EDA','ML']
    choice = st.sidebar.selectbox('메뉴 선택', menu)

    if choice == menu[0]:
        run_home_app() # ctrl+클릭하면 실행할(연결된) 부분으로 바로 이동하여 유지보수에 용이하다
    elif choice == menu[1]:
        run_eda_app()
    elif choice == menu[2]:
        run_ml_app()

if __name__ == '__main__':
    main()
