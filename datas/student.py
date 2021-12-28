# 학생 정보를 담고, 기능들을 가진 클래스

class Student:
    # 학생 객체를 만들 때, 이름 / 출생년도(int) / 거주지를 받아서 세팅해주자
    def __init__(self, name, birth_year, address):
        self.name = name
        self.birth_year = int(birth_year)    # str이 들어온 경우를 대비한다
        self.address = address

    
    # 나이를 계산해주는 기능 추가(2021년 기준)
    def get_age(self):     # 파라미터값에 birth_year은 안들어감 왜냐 이미 self에 담겨있기 때문.. 세상에 깨달음!
        return 2021 - self.birth_year + 1
    
    
    # 정보를 가공해서 출력(print)기능 추가 = return X
    def print_student_info(self):
        print(f'{self.name}({self.get_age()}세) - {self.address}')