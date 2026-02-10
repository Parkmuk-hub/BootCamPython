"""
주차 요금 계산 프로그램 문제
1. 조건

부품 클래스 (Calculator)

변수: pricePerMinute = 100 (1분당 100원)

메소드: calculate(time)

주차 시간(분)을 입력받아 시간 * 100을 계산합니다.

결과값(요금)을 return 합니다.

본체 클래스 (ParkingManager)

생성자: Calculator 객체를 멤버 변수로 생성(포함 관계).

메소드: start()

사용자에게 차량 번호와 **주차 시간(분)**을 입력받습니다.

부품 객체의 calculate를 호출하여 요금을 받습니다.

최종 결과를 출력합니다.

2. 출력 형태 예시

Plaintext
차량 번호를 입력하세요 : 123가4567
주차 시간(분)을 입력하세요 : 60
------------------------------
차량 123가4567의 주차 요금은 6000원입니다.
💡 힌트 순서

Calculator 클래스를 먼저 정의하고 return을 사용해 요금을 반환하게 만드세요.

ParkingManager의 __init__에서 self.cal = Calculator()를 넣어 부품을 장착하세요.

start 메소드에서 self.cal.calculate(주차시간) 처럼 부품에게 일을 시키고 그 결과를 변수에 담아 print 하세요.
"""
class Calculator :
    def __init__(self):
        self.price = 100

    def cal(self, time) :
        return time * self.price


class Parking :
    def __init__(self):
        self.Calc = Calculator()

    def start(self) :
        self.time = int(input("주차 시간을 입력하세요 :"))
        num = input("차량 번호를 입력하세요 :")
        sum = self.Calc.cal(self.time)
        print("-" * 30)
        print(f'차량{num}의 주차 요금은 {sum}')


money = Parking()
money.start()