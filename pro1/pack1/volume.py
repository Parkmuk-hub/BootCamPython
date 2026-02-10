class ElecProduct :
    def __init__(self) :
        self.volume = 0

    def volumeControl(self, volume) :
        self.volume = volume
        

class ElecTv(ElecProduct) :
    
    def volumeControl(self, volume):
        super().volumeControl(volume)
        sori = self.volume
        if self.volume >= 50 :
            print(f"듣기 좋아요 : {sori}")
        else :
            print(f"너무 조용해요 : {sori}")

class ElecRadio(ElecProduct) :
        
    def volumeControl(self, volume):
        super().volumeControl(volume)
        sound = self.volume
        if self.volume >= 50 :
            print(f"소리를 줄여라 : {sound}")
        else :
            print(f"소리를 높여라 : {sound}")

Elec = ElecProduct()
Elec1 = ElecTv()
Elec = Elec1
Elec.volumeControl(40)
Elec2 = ElecRadio()
Elec = Elec2
Elec.volumeControl(40)

print("\n ____________________")
q1 = [ElecTv(), ElecRadio()]
for a in q1 :
    a.volumeControl(2)


"""
부모 클래스 ElecProduct에서 메소드volumeContorl 안에 volume 값을 설정해주고
자식 클래스 ElecTv, ElecRadio는 volumeControl을 오버라이딩 하되 
volume 값은 super().volumeControl(volume)를 통해 부모의 메소드에서 전달 받는다

"""
"""
메소드 오버라이딩: 자식 클래스(ElecTv, ElecRadio)가 부모 클래스의 volumeControl 메소드를 
자신만의 로직으로 재정의한 점이 명확합니다.

super()의 역할: 자식 클래스에서 데이터를 직접 수정하지 않고, 부모의 기능을 호출하여 상태를 
변경한 뒤 추가 로직을 수행하는 방식은 객체지향 프로그래밍에서 권장되는 "확장" 방식입니다.

데이터의 흐름: volume 값은 super().volumeControl(volume)을 통해 부모 클래스의 인스턴스 변수에 먼저 저장되고
, 그 저장된 값을 다시 자식 클래스에서 꺼내어(if self.volume >= 50) 판단 기준으로 사용하는 흐름이 매끄럽습니다.

🔍 사소하지만 중요한 팁
코드의 구조상 문제는 없지만, 한 가지 더 알아두시면 좋은 점이 있습니다.

인스턴스 변수 초기화: 현재 코드에서는 volume = 0이 클래스 변수로 선언되어 있습니다. 
보통 객체마다 독립적인 볼륨 값을 가지게 하려면 __init__ 메소드를 사용하는 것이 더 안전합니다.
"""
