# 클래스의 다중 상속 - 부모가 복수

class Tiger :
    data = "호랑이 세계"

    def cry(self) :
        print('호랑이 : 어흥')

    def eat(self) :
        print("맹수는 고기를 먹는다")

class Lion :
    def cry(self) :
        print("사자 : 으르렁")

    def hobby(self) :
        print("백수의 왕은 낮잠이 취미")

# Tiger과 Lion 둘다 super class

class Liger1(Tiger, Lion) : # ***다중 상속은 순서가 중요하다.***
    pass
# 메소드가 중복될 경우 먼저 적은 class의 메소드를 사용함.

a1 = Liger1()
print(a1.data) #호랑이 세계
a1.cry() #호랑이 : 어흥
a1.eat()
a1.hobby() # 백수의 왕은 낮잠이 취미
print("\n",'________',"\n")

def hobby():
    print("모듈의 멤버 : 일반함수")

class Liger2(Lion, Tiger) :
    data = "라이거 만세"

    def play(self) :
        print("라이거 고유 메소드입니다")

    def hobby(self) : # Method Override
        print("라이거는 공원 걷기를 좋아함")

    def showData(self) :
        self.hobby() #Liger2 hobby  [라이거는 공원 걷기를 좋아함]
        super().hobby() #Lion hobby [백수의 왕은 낮잠이 취미]
        hobby() # class 밖 모듈의 hobby [모듈의 멤버 : 일반함수]

        self.eat() #Liger2에서 찾고 없으면 Lion -> Tiger 찾음 [맹수는 고기를 먹는다]
        super().eat() # 처음부터 Lion -> Tiger [맹수는 고기를 먹는다]

        print(self.data + ' ' + super().data) # [라이거 만세 호랑이 세계]

a2 = Liger2()
a2.cry() #사자 : 으르렁 <== Lion을 먼저씀
a2.showData()
        