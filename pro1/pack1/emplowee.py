from abc import *

class Employee(metaclass=ABCMeta) :
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai

    @abstractmethod
    def pay(self) :
        pass
    
    @abstractmethod
    def data_print(self) :
        pass
    
    def irumnai_print(self) :
        print('이름: ' + self.irum + ',나이:', str(self.nai), end = ' ')

class Temporary(Employee) : 
    def __init__(self, irum, nai, ildang, ilsu):
        Employee.__init__(self, irum, nai)
        self.ildang = ildang
        self.ilsu = ilsu

    def pay(self) :
        return self.ildang * self.ilsu

    def data_print(self) :
        self.irumnai_print()
        print(', 월급: ' + str(self.pay()))

class Regular(Employee) :
    def __init__(self, irum, nai, salary):
        Employee.__init__(self, irum, nai)
        self.salary = salary

    def pay(self) :
        return self.salary

    def data_print(self) :
        self.irumnai_print()
        print(', 급여: ' + str(self.pay()))

class Saleman(Regular) :
    def __init__(self, irum, nai, salary, sales, commission):
        Regular.__init__(self, irum, nai, salary)
        self.sales = sales
        self.commission = commission

    def pay(self) :                            
        
        return self.salary + (self.sales * self.commission)
    
    def data_print(self):
        self.irumnai_print()
        print(', 수령액: ' + str(round(self.pay())))
        

t = Temporary('홍길동', 25, 20, 150000)
t.data_print()

r = Regular("한국인", 27, 3500000)
r.data_print()

s = Saleman("손오공", 29, 1200000, 5000000, 0.25)
s.data_print()