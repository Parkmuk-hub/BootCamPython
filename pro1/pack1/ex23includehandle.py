print("\n",'__________________________________________________',"\n")
# 어딘가에서 필요한 부품 핸들 클래스 작성
class includeHandle :
    quantity = 0 # 핸들 회전량, 클래스 변수 -> 공유자원

    def leftTurn(self, quentity) : # quentity : 지역 변수
        self.quantity = quentity # self 나 leftTurn이 안붙었으면 0을 넣음 
        return "좌회전"
    
    def rightTurn(self, quentity) :
        self.quantity = quentity
        return "우회전"
    
