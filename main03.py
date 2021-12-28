# 절대 경로 체험

my_file = open('c:\\202112_EunHyung_Python\\file_test\\my_test3.txt', 'r')  # r : read 읽어오기 모드

# 파일 내용 전부 읽고 싶다 => 몇 줄이 전부일까? 알 수 없음
# 반복 횟수 불명확함 => while True + if break 용법 활용
while True:
    line = my_file.readline()
    
    # 내용 출력 : 읽어온 내용이 있어야 의미있는 행위
    # 읽어온 내용에 아무것도 없다 : 반복 종료
    if not line:
        print('파일을 끝까지 읽었습니다.')
        break
     
    print(line, end = '')
    
my_file.close()
