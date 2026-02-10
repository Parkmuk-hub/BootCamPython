# 기본 자료형 : int, float, bool, complex
# 묶음 자료형 : str, list, tuple, set, dict

#1) str : 문자열 묶음 자료형, 순서 있지만 수정이 불가능
s = 'sequence'
print(s, id(s))
print(' 길이 :', len(s))
print(s[0], s[2])
print(' 길이 :', s.find('e'), s.find('e', 3), s.rfind('e')) # s.find('찾고싶은문자', 몇 번째 인덱스부터 시작)
# 인덱싱 / 슬라이싱
print(s[5]) # 인덱싱 - 변수명[순서], index는 0부터 출발
print(s[2:5]) # 슬라이싱 변수[s:e:s]
print(s[:], ' ', s[0:len(s)], s[::1])
print(s[0:7:2])
print(s[-1], ' ', s[-4: -1: 1]) # -1은 맨뒤 , 맨앞은 0부터
print(s, id(s))
s = 'sequenc' # 수정아님 변경임
print(s, id(s))
s = 'bequence' 
print(s, id(s))

print('__________________________________________________',"\n")
#2) list : 다양한 종류의 자료 묶음형, 순서 있고 수정과 중복 가능
a = [1, 2, 3]
print(a, a[0], a[0:2])
b = [10, a, 10, 20.5, True, "문자열"]
print(b, ' ', b[1], ' ', b[1][0], "\n") # a리스트 첫 번째 요소 꺼내옴 [0번 인덱스]

family = ['어머니', '아빠', '나', '누나']
print(id(family))
family.append('남동생') # 변경이 아닌 수정(.append)
print(id(family))
family.remove('나') # 지정 문자 제거
family.insert(0, '할머니') # 첫 번째에 문자 삽입
family.extend(['삼촌', '고모', '조카']) # 추가
family += ['이모'] # 추가 
print(family)
print(family.index('아빠')) # 아빠 몇 번째 인지 찾기
print('어머니' in family, '나' in family)

family.remove('아빠')
del family[2]
print(family, "\n")

kbs = ['123', '34', '234']
kbs.sort() # 문자 정렬
print(kbs)

tvn = [123, 34, 234]
tvn.sort(reverse = True) # 숫자 정렬 reverse = True <- 역순
print(tvn)

sbs = [123, 34, 234]
mcn = sorted(sbs) # sorted <- 원본 값은 유지하고 정렬한 값은 현재 변수에 넣음
print(sbs)
print(mcn, "\n")

name = ['tom', 'holland', 'tony']
name2 = name
print(name, id(name))
print(name2, id(name2))

import copy
name3 = copy.deepcopy(name)
print(name3, id(name3))

name[0] = 'stark'
print(name, id(name))
print(name2, id(name2))
print(name3, id(name3))

print('__________________________________________________',"\n")

#3) tuple : 리스트와 유사하나 읽기 전용임. 수정 불가능
t = (1, 2, 3, 4)
t = 1, 2, 3, 4 # 위와 동일
print(t, type(t))

# k = (1)  요소 값 하나일 때 튜플이 되고싶으면 (요소1,) <- 튜플임
k = (1,)
print(k, type(k))
print(t[0], ' ', t[0:2])
# t[0] = 77 <- 'tuple' object does not support item assignment

imsi = list(t)
imsi[0] = 77
t = tuple(imsi)
print(t)

print('__________________________________________________',"\n")
#4) set : 수정과 중복이 불가능
ss = {1, 2, 1, 3}
print(ss)
ss2 = {3, 4}
print(ss.union(ss2)) # 합집합
print(ss.intersection(ss2)) # 교집합
print(ss - ss2, ss | ss2, ss & ss2) # 차, 합, 교집합
# print(ss[0]) <- TypeError: 'set' object is not subscriptable 순서가 없어 인덱싱과 수정이 불가능
ss.update({6, 7})
print(ss)
ss.discard(2) # 있으면 지우고 없으면 스킵 [예외처리 필요없음]
ss.remove(6) # 있으면 지우고 없으면 오류 [예외처리 필요함]
print(ss)

li = ['aa', 'aa', 'bb', 'cc', 'aa']
print(li)
imsi = set(li) # li 리스트의 중복 제거, 순서는 랜덤
li = list(imsi)
print(li)

print('__________________________________________________',"\n")
#5) dict : 사전 자료형 {'키': 값} 형태
# 방법1
mydic = dict(k1 = 1, k2='ok', k3 =123.4)
print(mydic, type(mydic))

# 방법2
dic = {'파이썬':'뱀', '자바':'커피', '인사':'안녕'}
print(dic)
print(len(dic))
print(dic['자바']) # 키로 값을 검색
ff = dic.get('자바')
print(ff)
# print(dic['커피'])
# print(dic[0]) 인덱싱 없음
dic['금요일'] = '와우' # 추가
print(dic)

del dic['인사'] # 삭제
print(dic)
print(dic.keys()) # 키 값만 출력
print(dic.values()) # 값만 출력

print("-----------------------------------정규 표현식을 기억하자--------------------------------------")