class Car :
    handle = 1 # 멤버 변수
    speed = 0 

    def __init__(self, name, speed) :
        self.name = name # <== 현재 객체의 name에게 name(지역 변수) 인자값 치환
        self.speed = speed

    def showData(self) : # self 있으면 메소드 없으면 아님
        km = "킬로미터"
        msg = '속도 : ' + str(self.speed) + km
        return msg
    
    def printHandle(self) :
        return self.handle # 원형 클래스 값 1을 바로 찾아가는게 아니라 돌아간다

    
print(Car.handle) # 원형(prototype) 클래스의 멤버 호출
car1 = Car('tom', 10) # 생성자 호출 후 객체 생성(인스턴스화)
print('car1 객체 주소 :', car1)
print('car1 : ', car1.name, ' ', car1.speed, car1.handle)
car1.color = '파랑' # <== car1 객체 안에 color 라는 멤버가 추가됨
print(car1.color)

car2 = Car('John', 20)
print('car2 객체 주소 :', car2)
print('car2 : ', car2.name, ' ', car2.speed, car2.handle)

print(Car, car1, car2)
print(id(Car), id(car1), id(car2)) # 3개의 주소가 각각 다름
print(car1.__dict__)
print(car2.__dict__) # 각각 자신의 멤버를 확인할 수 있음

print("\n",'__________________________________________________',"\n")
print('메소드 : ')
print('car1 speed : ', car1.showData())
print('car2 speed : ', car2.showData())
car1.speed = 80
car2.speed = 110
print('car1 speed : ', car1.showData())
print('car2 speed : ', car2.showData())
print('car1 handle : ', car1.printHandle())
print('car2 handle : ', car2.printHandle())
"""
Car[prototype (원형 클래스)] 라는 클래스 안에
handle = 1, name, speed = 0 라는 멤버 변수
(멤버 변수 앞에 +, - 붙일 수 있고 공유한다 안한다를 나타냄, 멤버 메소드는 없음)
showData(self) 라는 멤버 메소드를 가지고있음
모든 멤버들은 공유 가능함.

Car.handle을 직접 호출하면 Car 클래스 안에 handle 값을 출력함
car1 = Car('tom', 10) <== skip된 self안에 car1 주소가 들어가있음, Car 클래스의 객체가 하나 생성됨.
입력한 'tom'은 self.name에 저장되는데 self는 car1의 주소가 저장됨. self.name = name은 
car1에서 tom을 꺼내옴, speed도 마찬가지로 이렇게 꺼내옴
car1.handle은 지역변수인 car1 주소 안에서 값을 찾다가 없으면 원형 클래스인 Car로 돌아가 값을 찾음

항상 지역변수 먼저 찾아보고 없으면 원형 클래스를 참고해서 값을 꺼내옴
"""

"""
"Class Diagram, UseCase Diagram, Sequence Diagram"
"""