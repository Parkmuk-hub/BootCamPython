class Animal :
    def __init__(self):
        self.name = "동물"
    def move(self) :
        print("나는 동물입니다.")

class Dog(Animal):
    name = "개"
    def __init__(self):
        self.name = "라떼"

    def move(self) :
        print(f"나는 {self.name}입니다.")

class Cat(Animal) :
    name = "고양이"
    def __init__(self, name):
        self.name = name

    def move(self) :
        print(f"나는 {self.name}입니다.")

class Wolf(Dog, Cat, Animal) :
    pass

class Fox(Cat, Dog, Animal) :
    def __init__(self, name):
        super().__init__(name)
        self.name = name
    def move(self) :
        print(f"욕심쟁이 {self.name}입니다.")

    def foxMethod(self) :
        print("여우 전용 메소드입니다.")

an = Animal()
an.move()

do = Dog()
do.move()

ca = Cat("앙고")
ca.move()

fo = Fox("패트")
fo.move()
fo.foxMethod()

wo = Wolf()
wo.move()

print("\n _______")
#animal = [Dog(), Cat(), Fox(), Wolf()]
#for a in animal :
#    a.move()