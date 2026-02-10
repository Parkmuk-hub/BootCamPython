kor = 100 # 모듈의 전역 변수

def abc() :
    kor = 0 # 함수 내의 지역 변수
    print('모듈의 멤버 함수')

class My :
    kor = 80 # My 멤버 변수(필드)

    def abc(self) :
        print('My 멤버 메소드')

    def show(self) :
    #  kor = 77 # 메소드 내의 지역 변수
        print(kor) # 모듈의 전역 변수를 가져다씀 클래스 내의 전역 변수를 쓰고 싶으면 self 나 My를 붙여야함
        self.abc() # My 클래스 내부의 abc 출력
        abc() # class 밖에 있는 abc 출력

my = My()
my.show()
print("\n",'__________________________________________________',"\n")
print(My.kor)

tom = My()
print(tom.kor) # 80이 출력 My 필드안의 멤버 변수가 80임
tom.kor = 88 # tom이라는 객체 내부에만 88을 저장
print(tom.kor)

oliver = My()
print(oliver.kor)



"""
self를 붙혀서 사용하면 class 내의 멤버 변수를 찾아 출력하고
그냥 사용하면 모듈의 전역 변수를 출력함
"""
"""
1. 파이썬의 변수 찾기 여정 (Scope)show 메소드 안에 print(kor)라는 문장을 만났을 때, 파이썬은 **"주소지"**가 명시되지 않았으므로 아래 순서대로 kor를 찾아 헤맵니다.
메소드 안(Local): "혹시 show 안에 kor = 77 같은 지역 변수가 선언되어 있나?"  -> 없음 (주석 처리됨)
클래스 안(Class): "그럼 My 클래스 변수인가?" -> 무시함. (중요: 파이썬은 self.이나 My. 같은 명시적 지시가 없으면 클래스 내부를 자동으로 뒤지지 않습니다.)
파일 전체(Global): "그럼 이 파일(모듈) 전체에서 쓰는 전역 변수인가?" -> 발견! (kor = 100)

2. 만약 80을 출력하고 싶었다면?코드를 아래 중 하나로 수정해야 파이썬이 클래스 쪽을 쳐다봅니다.
print(self.kor) : "나(my)의 주머니를 보고, 없으면 내 설계도(My)를 봐!" -> 80 출력
print(My.kor) : "내 설계도(My)에 적힌 값을 바로 가져와!"  -> 80 출력
"""
