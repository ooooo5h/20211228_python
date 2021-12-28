# student_list.txt 파일에 저장된 학생 정보들을 하나씩 출력

with open('student_list.txt', 'r') as f:
    # f -> readlines()  -> 모든 줄을 list로 담아서 리턴
    
    student_info_list = f.readlines()
    
    # 목록 반복 -> 한줄씩 출력
    for student_info in student_info_list:
        
        # student_info str 끝에는 \n이 달려있다 => 임시 제거 처리
        student_info = student_info.strip()
        
        print(student_info)