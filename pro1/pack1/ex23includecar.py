# 여러 개의 부품 객체를 조립해 완성차 생성
# 클래스의 포함 관계 사용 (자원의 재활용 [객체지향 프로그래밍 핵심])
# 다른 클래스(Object)를 마치 자신의 멤버처럼 선언하고 사용
# class => 객체{Object}, instance
print("\n",'__________________________________________________',"\n")
#import ex23includehandle
from ex23includehandle import includeHandle

class includeCar :
    turnShowMessage = "정지"

    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = includeHandle() # 클래스 포함 관계

    def turnHandle(self, q) :
        if q > 0 :
            self.turnShowMessage = self.handle.rightTurn(q) # q 가 includeHandle 클래스의 지역 변수(quantity)값을 건듬
        elif q < 0 :
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q == 0 :
            self.turnShowMessage = 0

if __name__ == '__main__' : # 클래스 호출했을 때 이거 써주는게 좋음, 안써도 ㄱㅊ
    tom = includeCar('Mr.Holland')        
    tom.turnHandle(10)
    print(tom.ownerName + '의 회전량은 :', tom.turnShowMessage + ' ', str(tom.handle.quantity))
print("\n",'__________________________________________________',"\n")

john = includeCar("Mr.Fleck")
john.turnHandle(-20)
print(john.ownerName + '의 회전량은 :', john.turnShowMessage + ' ', str(john.handle.quantity))

"""
1. self.handle = includeHandle() 부분
주석: 클래스 포함 관계

보완: 아주 정확합니다! 이를 Has-a 관계라고도 합니다. "자동차(Car)가 핸들(Handle)을 가지고 있다"는 논리죠. 
다른 클래스의 인스턴스를 내 멤버 변수에 할당하여 그 기능을 가져다 쓰는 객체지향의 핵심 기법입니다.

2. self.handle.rightTurn(q) 부분
주석: q 가 includeHandle 클래스의 지역 변수(quantity)값을 건듬

보완: 이 부분은 용어를 살짝 수정하면 완벽해집니다.

q는 rightTurn 메소드에 전달되는 **인자(Argument)**입니다.

quantity는 includeHandle 클래스의 멤버 변수(정확히는 인스턴스 변수)입니다.

즉, **"차(Car) 객체가 핸들(Handle) 객체의 메소드를 호출하여, 핸들 객체 내부의 상태값(quantity)을 변경시킨다"**고 이해하시면 됩니다.

3. if __name__ == '__main__': 부분
주석: 클래스 호출했을 때 이거 써주는게 좋음, 안써도 ㄱㅊ

보완: 실무적으로 매우 중요한 습관입니다!

이 주석의 의미를 좀 더 구체화하면: **"이 파일이 직접 실행될 때만 테스트 코드를 돌리고, 
다른 파일에서 import 될 때는 클래스 설계도만 넘겨주고 실행은 하지 마라"**는 뜻입니다.
"""
