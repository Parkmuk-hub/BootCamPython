# 상속

class Person :
    say = '난 사람이야~~' # 접근 권한 = public
    nai = '26'
    __msg = 'good : private-member' # 현재 클래스에서만 동작

    def __init__(self, nai):
        print("Person 생성자")
        self.nai = nai

    def printInfo(self) : # 접근 권한 = public
        print(f'나이:{self.nai}, 이야기:{self.say}')

    def helloMethod(self) :
        print('안녕')
        print("hello :", self.say, self.nai, self.__msg)

print(Person.say, Person.nai)
# Person.printInfo() <== 이건 안돼
per = Person('25')
per.printInfo()
per.helloMethod() # <== 이건 된다
print("\n",'________',"\n")

class Employee(Person) : 
    subject = '근로자' #emp.subject
    say = 'yes'   # hiding, shadowing
    def __init__(self):
        print('Employee 생성자')
    def printInfo(self):
        print('Employee 클래스의 printInfo 호출됨')

    def ePrintInfo(self) : 
        print(self.subject, self.say, self.nai) # say를 출력함 <== local 우선탐색
        # print(self.__msg) # __private 멤버() : Person에서만 유효
        self.helloMethod() # 자신에게 없으면 부모한테 가서 찾음
        self.printInfo() # hiding, shadowing <== local 우선탐색
        print(super().say) # super == 부모 값 바로 호출
        super().printInfo() # super().부모의 멤버
        
emp = Employee()
print(emp.subject, emp.nai)
emp.ePrintInfo()
# emp.printInfo()
print("\n",'________',"\n")

class Worker(Person) :
    def __init__(self, nai):
        print('Workder 생성자')
        super().__init__(nai) # 부모 클르새의 생성자 명시적 호출 

    def wPrintInfo(self) :
        print('Worker - wPrintInfo 처리')
        super().printInfo()

wok = Worker('30') # 부모 클래스 self.nai에서 30을 받고 내려옴
print(wok.say, wok.nai)
wok.wPrintInfo()
print("\n",'________',"\n")

class Programmer(Worker) :
    def __init__(self, nai):
        print('Programmer 생성자')
        # super().__init__(nai) # Bound call
        Worker.__init__(self, nai) # UnBound call

    def pPrintInfo(self) :
        print('Programmer - pPrintInfo 처리했음')
    
    def wPrintInfo(self) : # 부모 메소드와 동일 메소드 선언
        print('Programmer에서 overriding')

pro = Programmer('36')
print(pro.say, pro.nai)
pro.pPrintInfo()
pro.wPrintInfo()
print("\n",'________',"\n")

print("클래스 타입 확인")
a = 3; print(type(a)) # <class 'int'>
print(type(pro)) # <class '__main__.Programmer'>
print(type(wok)) # <class '__main__.Worker'>
print(Person.__bases__) # (<class 'object'>,)
print(Employee.__bases__) # (<class '__main__.Person'>,)
print(Worker.__bases__) # (<class '__main__.Person'>,)
print(Programmer.__bases__) # (<class '__main__.Worker'>,)

"""
다형성 구사 = 상속
다형상 구사x = 포함
"""