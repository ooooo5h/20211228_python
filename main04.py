# 파일은 열고 나면 반드시 닫아야함
# 파이썬의 with 문법 이용하면, 열고 난 파일을 with 구문이 끝나면 자동으로 종료처리

with open('student_list.txt', 'a') as my_file:    # a : 추가 작성이지만, 해당 파일이 없다면 생성도 같이 진행해줌

    # 새 학생을 한명씩 추가하자
    # 이름, 출생년도, 거주지 (ex. 서울시 동대문구)
    print('새 학생 추가')
    
    name = input('이름 : ')
    birth_year = int(input('출생년도 : '))
    address = input('거주지 : ')
    
    # 파일에 한 줄의 문구로 추가 = 이름, 년도, 거주지 한 줄로 가공해서 파일에 추가하고싶다
    input_line = f'{name}, {birth_year}, {address}'
    print(input_line)
    
# with 구문이 끝남
# 여기가 실행된다 : my_file은 자동으로 close되어있는 상태