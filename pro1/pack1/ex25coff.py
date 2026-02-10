class CoinIn :
    def __init__(self):
        self.coin = 0
        self.change = 0 
    
    def culc(self, cupCount) : 
        total = cupCount * 200

        if self.coin < total :
            return "요즘이 부족합니다."
        else :
            self.change = self.coin - total
            return f'커피: {cupCount}잔과 잔돈: {self.change} 원'
            
        


class Machine :
    def __init__(self) :
        self.cupCount = 1
        self.inCo = CoinIn()

    def showData(self) :
        self.inCo.coin = int(input("동전을 입력하세요 :"))
        self.cupCount = int(input("몇잔을 원하세요 :"))

        result = self.inCo.culc(self.cupCount)
        print(result)

coffee = Machine()
coffee.showData()

"""
다이어그램에서 CoinIn 클래스 안에 변수는 coin과 change 두개에 culc 메소드 cupCount 만 사용
CoinIn의 두 변수는 self를 통해 머신에서 입력받아 사용하고 culc메소드는 계산식을 만든다
완성된 CoinIn클래스는 Machine 클래스에서 호출해서 사용하고 showData 메소드에서 coin을 호출해 동전을 입력 받습니다.
cupCount에 잔 개수를 입력받아 CoinIn 클래스 culc 메소드에 넣는다
Machine의 showData()를 호출하면 실행된다.
"""
        
        


