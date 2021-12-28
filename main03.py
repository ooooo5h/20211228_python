# 절대 경로 체험

my_file = open('c:\\202112_EunHyung_Python\\file_test\\my_test3.txt', 'r')  # r : read 읽어오기 모드

line = my_file.readline()
print(line)

line2 = my_file.readline()
print(line2)

my_file.close()
