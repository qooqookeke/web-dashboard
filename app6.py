import streamlit as st

def main() :
    # 텍스트를 입력받는 방법
    name = st.text_input('이름을 입력하세요')
    st.subheader('제 이름은 ' + name + '입니다.')

    # st.text_input('이름 입력', value='홍길동')
    st.text_input('이름 입력', max_chars=5) # max_char: 글자수 제한
    st.text_input('이름 입력', max_chars=5, placeholder='홍길동') # placeholder: 텍스트입력 예

    text = st.text_area('메세지를 입력하세요.')
    st.text(text)

    # 숫자 입력 받는 방법
    st.number_input('출생연도를 입력하세요')  # 아무설정 안하면 소수점으로 나옴
    birth_year = st.number_input('출생연도를 입력하세요', 1900, 2023) 
    # str/min_value/max_value 순으로 작성
    st.text('저의 출생연도는 ' +str(birth_year)+ '입니다.')
    st.number_input('실수를 입력하세요', -2.0, 100.0, step=0.5)

    # 날짜 입력받는 방법
    my_date = st.date_input('약속 날짜 입력') # 디폴트 현재 날짜
    print(my_date)
    # st.text(my_date)
    print(type(my_date)) # 날짜 타입으로 표시
    # st.text(type(my_date))

    # "2023년 11월 21일 월요일 입니다." 라고 웹화면에 표시하기
    st.text(my_date.strftime('%Y년 %m월 %d일 %A 입니다.'))
    # 요일 영어로 표시되는 부분은 조건문으로 변경해야 함
    # ex. if Monday = '월요일' 이런 식으로

    # 시간 입력 받는 방법
    my_time = st.time_input('약속 시간 선택')
    print(type(my_time))
    st.text(my_time.strftime('%H:%M 에 약속 시간을 잡았습니다.'))

    # 비밀번로 입력받는 방법
    password = st.text_input('비밀번호 입력', type='password')
    print(password)

    # 색깔 입력
    color = st.color_picker('색을 선택하세요')
    st.text(color) # default_value: black
    

if __name__ == '__main__':
    main()