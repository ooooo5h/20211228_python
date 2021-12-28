# student_list.txt 파일에 저장된 학생 정보들을 하나씩 출력

with open('student_list.txt', 'r') as f:
    # f -> readlines()  -> 모든 줄을 list로 담아서 리턴
    
    student_info_list = f.readlines()
    
    # 목록 반복 -> 한줄씩 출력
    for student_info in student_info_list:
        
        # student_info str 끝에는 \n이 달려있다 => 임시 제거 처리
        student_info = student_info.strip()
          
        # 조경진(34세) - 서울시 동대문구 거주   양식으로 가공해서 출력
        # student_info를 ',' 기준으로 쪼개줘야 이름/출생년도/거주지를 분리해서 얻을 수 있다 => 구글링
        student_infos = student_info.split(',')   # ,를 기준으로 나눠서, 나온 목록을 변수에 저장
        
        # 이름 / 나이(int , 출생년도 활용) / 거주지
        name = student_infos[0]
        age = 2021 - int(student_infos[1]) + 1
        address = student_infos[2]
        
        info_str = f'{name}({age}세) - {address}'
        print(info_str)