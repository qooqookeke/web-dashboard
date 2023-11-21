import streamlit as st

# 스트림릿 프레임워크는 main 함수가 있어야 한다

def main(): # 함수의 정의
    # st는 웹 화면에 표시하는 역할을 한다
    st.title('헬로우')

if __name__=='__main__': # 조건문 / __name__ : 시스템 변수
    print(__name__)
    main() # 함수 호출, 함수 선택 후 ctrl+클릭 : 실행되는 함수로 이동

    # ctrl + c = 터미널 cmd 실행 종료

    