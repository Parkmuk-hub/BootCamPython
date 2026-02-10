# pack1/ex15module - main <== 써주는걸 적극 추천

print('사용자 정의 모듈 처리하기.')

s = 20 # 뭔가를 하다가 모듈이 필요해짐!

print('\n 경로 지정 방법1 : import 모듈명')
import pack1.mymod1 # 보조기억장치에 있는 모듈을 로딩 사용하려면 무조건 import

print(dir(pack1.mymod1)) # mymod1 안에 있는 멤버를 확인할 때 사용
print(pack1.mymod1.__file__) # 경로 및 파일명을 알려줌
print(pack1.mymod1.__name__) # 모듈명을 알려줌

list1 = [1, 2]
list2 = [3, 4, 5]
pack1.mymod1.listHap(list1, list2) 

if __name__ == '__main__' : print('나는 메인모듈__') 
# 실행하는 녀석이 메인 모듈이고, 가져다쓰면 메인아님 

print('\n경로 지정 방법2 : from 모듈명 import 함수명 또는 변수, ...')

from pack1.mymod1 import tvn, kbs,tot
tvn()
kbs()
print(tot)

from pack1.mymod1 import * # *을 사용해 mymod1 모듈의 모든 메머 로딩(이름 겹치는거 때문에 비권장)
print('tot : ', tot)

from pack1.mymod1 import tvn as 재미없다 # as하면 별명으로 쓸 수 있음
재미없다()

print('\n경로 지정 방법3 : import 하위 패키지.모듈명')

import pack1.subpack.sbs
pack1.subpack.sbs.sbsNews()

import pack1.subpack.sbs as nickname
nickname.sbsNews()

print('\n경로 지정 방법4 : 현재 package와 동등한 다른 package 모듈 읽기')

# import ../pack1_other.mymod2 vscode는 인정하지않음
from pack1_other import mymod2, mymod3
mymod2.hapFunc(3, 4)

import mymod3
result = mymod3.gopFunc(4, 3)
print('path가 설정된 곳의 module 읽기 - result :', result)
# pack1에서 나가서 python -m 패키지명.모듈명으로 실행 + 사용하는 모듈에 패키지명. 을 붙여야함
print('end')