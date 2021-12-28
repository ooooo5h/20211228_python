# 절대 경로 체험

my_file = open('c:\\202112_EunHyung_Python\\file_test\\my_test3.txt', 'r')  # r : read 읽어오기 모드

# my_file의 모든 내용을 미리 파악해둔다면? 필요한 만큼 반복 돌리면 된다
# 미리 파악 => readlines() => 모든 줄을 미리 읽어서, list로 담아준다

line_list = my_file.readlines()

# 리스트 내부의 요소들을 반복으로 뽑아내서 출력해보자
# for문의 정석 방법
for line in line_list:
    print(line)
    
my_file.close()
