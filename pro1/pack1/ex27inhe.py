# 상속 : 자원의 재활용을 목적으로 특정 클래스의 멤버를 가져다 쓰는것
# 코드 재사용
# 확장성 -  기존 클래스에 새 기능을 추가한 새로운 클래스 생성
# 구조적 설계 - 공통개념은 부모 클래스, 구체적 내용은 지식 클래스에서 구현
# 다형성 구사 - 메소드 오버라이딩

class Animal : # 동물들이 가져야할 공통 속성과 행위 선언
    # Animal = 부모, 조상, super, parent    
    age = 7
    
    def __init__(self):
        print('Animal 생성자')

    def move(self) :
        print('움직이는 생물')


class Dog(Animal) : # 부모 클래스로 하고싶은 것을 (클래스명) 합니다.
    # Dog = 자식, 자손, 파생, sub, child
    def __init__(self):
        print('Dog 생성자')
        

    def my(self) :
        print('라떼라고 합니다.')

        

dog1 = Dog()
dog1.my()
dog1.move() # Dog 클래스를 먼저 확인하고 없으면 부모 클래스 확인
print('age :', dog1.age) # 상속은 부모 클래스것을 내꺼마냥 사용함
print("\n",'________',"\n")

dog2 = Dog()
dog2.my()
dog2.move()
print("\n",'________',"\n")

class Horse(Animal) :
    pass

horse1 = Horse()
horse1.move()
print(horse1.age)

"""
클래스 강결합 = 상속, 약결합 = 포함/합성
부모 클래스(1개) = 단일 상속
부모 클래스(2개 이상) = 다중 상속 [자바 불가능]
"""