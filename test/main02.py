# 파일 만들기 테스트 - 상대경로

# 상위 폴더에 파일을 만들고 싶다 => .. 상위 폴더로 나가기
my_file = open('../테스트폴더에서만든파일.txt', 'w')

my_file.write('테스트\n')

my_file.close()