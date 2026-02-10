# 추상 클래스(abstract class)
# 추상 메소드를 가진 클래스를 추상 클래스라고 하며,
# 얘는 인스턴스 할 수 없다. 객체 생성 불가.
# 부모 클래스로만 사용됨

from abc import *

class AbstractClass(metaclass=ABCMeta) : # 추상 클래스
    @abstractmethod
    def abcMethod(self) : # 추상 메소드 : 오버라이딩 필수
        pass  
        
    def normalMtehod(self) : # 일반 메소드 : 얘는 선택
        print("추상 클래스 내의 일반메소드")

#parent = AbstractClass() # 에러 : 추상 클래스는 객체 생성 불가

class Child1(AbstractClass) : # 추상 클래스를 부모 클래스로 지정하고 추상메소드를 오버라이딩 안하면 그 클래스는 추상클래스
    name = "난 Child1"

    def abcMethod(self) :
        print('부모가 가진 abcMethod 재정의 : 강요당함;;')

c1 = Child1()
print('name :', c1.name)
c1.abcMethod()
c1.normalMtehod() # child1에 없어서 부모클래스로 올라가서 찾음 

class Child2(AbstractClass) :
    def abcMethod(self) :
        print('추상 클래스 내의 abcMethod 재정의')

    def normalMtehod(self) : # 일반 메소드 재정의 (오버라이딩)
        print("일반메소드 내 맘대로 내용 변경") 

c2 = Child2()
c2.abcMethod()
c2.normalMtehod() # 얘는 안해도되는걸해서 본인이 가지고있음 부모 클래스로 안올라감
print("\n",'________',"\n")

happy = c1
happy.abcMethod()
happy = c2
happy.abcMethod()
happy.normalMtehod()
