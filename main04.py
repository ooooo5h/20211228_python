# 파일은 열고 나면 반드시 닫아야함
# 파이썬의 with 문법 이용하면, 열고 난 파일을 with 구문이 끝나면 자동으로 종료처리

with open('student_list.txt', 'a') as my_file:    # a : 추가 작성이지만, 해당 파일이 없다면 생성도 같이 진행해줌
    my_file.write('이 파일은 학생 목록을 저장합니다.')
    
# with 구문이 끝남
# 여기가 실행된다 : my_file은 자동으로 close되어있는 상태