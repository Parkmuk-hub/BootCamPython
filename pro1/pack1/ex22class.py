print("\n",'__________________________________________________',"\n")
# 클래스는 새로운 탕비을 만들어 자원을 공유 가능

#class Singer :
#   title_song = "빛나라 대한민국"
#
#   def sing(self) :
#        msg = "노래는"
#       print(msg, self.title_song)

# import ex22singer <== 이거 쓰면 클래스 선언 앞에 ex22singer. 을 붙여야함. 
from ex22singer import Singer # 변수앞에 주소를 하나하나 붙이기 귀찮을 때 사용

bts = Singer()  # 생성자 호출해 객체 생성 후 주소를 bts에 치환
bts.sing() # sing 변수에 print 실행 -> self를 붙혔기 떄문에 class 내부에서 변수를 찾아 사용
print(type(bts)) # <class '__main__.Singer'>
bts.title_song = "Permission to Dance" # bts 라는 객체에 노래를 넣음 클래스 내부 노래가 바뀌어도 고정
bts.sing()
bts.co = "빅히트 엔터테인먼트" # bts 라는 객체에만 소속사 추가
print('방탄 소속사 : ', bts.co)
print("\n",'__________________________________________________',"\n")
IVE = Singer()
IVE.sing()
print(type(IVE)) # <class '__main__.Singer'>
# IVE.title_song = "XOXZ"
IVE.co = "스타쉽 엔터테인먼트"
IVE.sing()
print('아이브 소속사 : ', IVE.co)
Singer.title_song = "국가대표" # IVE 는 객체에 따로 노래를 추가해주지 않았기 떄문에 class 노래 바꾸면 바뀜
bts.sing()
IVE.sing()
print("\n",'__________________________________________________',"\n")

niceGroup = IVE # IVE 에게 별명을 붙여줌
niceGroup.sing() 

"""
1. 아주 잘 파악하신 부분
from ... import ...: 모듈명을 매번 붙이지 않아도 되도록 경로를 생략해주는 편의성을 정확히 알고 계십니다.

객체 전용 속성 추가: bts.co = "..."처럼 파이썬은 실행 중에 특정 객체에만 새로운 변수(속성)를 추가할 수 있는 동적 타이핑 언어라는 점을 잘 활용하셨습니다.

클래스 변수 변경의 영향: Singer.title_song = "국가대표"라고 바꿨을 때, 자기만의 title_song을 가진 bts는 무시하고, 자기 것이 없는 IVE만 영향을 받는 원리를 정확히 이해하셨습니다.

2. 용어의 미세 조정 (더 완벽한 이해를 위해)

"bts 라는 객체에 노래를 넣음 클래스 내부 노래가 바뀌어도 고정"
보충: 이때 bts 객체 메모리 안에 title_song이라는 이름의 인스턴스 변수가 새로 생성됩니다. 이제 bts는 클래스 변수를 보러 가지 않고 자기 주머니에 있는 값을 먼저 꺼내 쓰게 됩니다.

"niceGroup = IVE 에게 별명을 붙여줌"
보충: 아주 좋은 표현입니다! 전문 용어로는 '얕은 복사(Shallow Copy)' 또는 **'참조 할당'**이라고 합니다. niceGroup과 IVE는 메모리 상의 같은 주소를 가리키게 되므로, niceGroup.co를 바꾸면 IVE.co도 같이 바뀝니다.
"""