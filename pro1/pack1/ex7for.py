# 반복문  for

#for i in [1, 2, 3, 4, 5] :
#for i in (1, 2, 3, 4, 5) :
for i in {1, 2, 3, 4, 5} :        
    print(i, end = ' ')

print('분산 / 표준편차')

numbers = [1, 3, 5, 7, 9]
tot = 0
for a in numbers :
    tot += a
print(f"합은 {tot}, 평균은 {tot / len(numbers)}")
avg = tot / len(numbers)
#편차의 합
hap = 0
for i in numbers :
    hap += (i - avg) **2
print(f'편차 제곱의 합 {hap}')
vari = hap / len(numbers)
print(f'분산은 {vari}')
print(f'표준 편차 {vari ** 0.5}')

print('__________________________________________________',"\n")
colors = ['r', 'g', 'b']
for v in colors :
    print(v, end = ' ')

print("\n")

print('iter() : 반복 가능한 객체를 하나씩 꺼낼 수 있는 상태로 만들어 주는 함수')

iterator = iter(colors)

for v in iterator :
    print(v, end = ', ')
print("\n")

for idx, d in enumerate(colors) : # enumerate : 인덱스와 값을 반환
    print(idx, ' ', d)
print("\n")

print("\n",'__________________________________________________',"\n")

print('사전형')
datas = {'python' : '만능언어', 'java' : '웹용언어', 'mariadb' : 'RDBMS'}
for i in datas.items() :
    #print(i)
    print(i[0], ' ~~ ', i[0])
print("\n")

for k, v in datas.items() :
    print(k, ' -- ', v)
print("\n")

for k in datas.keys():
    print(k, end = ' ')
print("\n")

for val in datas.values() :
    print(val, end = ' ')
print("\n")

print("\n",'__________________________________________________',"\n")

print("다중 for문")
for n in [2, 3] :
    print('--{}단--'.format(n))
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9] :
        print('{} * {} = {}'.format(n, i, n * i))
print("\n")
print("continue, break")
print("\n")

nums = [1, 2, 3, 4, 5]
for i in nums :
    if i == 2: continue
    if i == 4: continue
    print(i, end =' ')
else :  
    print('정상종료')

print("\n")
print("정규 표현식 + for")
print("\n")

str = """1일 우크라이나 드니프로페트로우스크주 테르니우카 주민들이 러시아군 드론 
공격을 받아 파괴된 우크라이나 에너지기업 DTEK의 통근버스 주변에서 시신을 수습하고 있다. 
이번 공격으로 퇴근하던 광부 중 최소 12명이 사망하고 16명이 부상당했다.
"""
import re
str2 = re.sub(r'[^가-핳\s]', ' ', str) # 한글과 공백 이외의 문자는 공백처리
print(str2)
str3 = str2.split(' ') # 공백을 기준으로 문자열 분리
print(str3)
cou = {}

for i in str3:
    if i in cou :
        cou[i] += 1 # 같은 단어가 있으면 누적
    else :
        cou[i] = 1 # 최초 단어인 경우는 '단어' : 1
print(cou)
print("\n")

print('정규 표현식 좀 더 연습')
print("\n")
for test_ss in ['111-1234', '일이삼-일이삼사', '222-1234', '333&1234'] :
    if re.match(r'^\d{3}-\d{4}$', test_ss):
        print(test_ss,'전화번호 맞음')
    else :
        print(test_ss, "전화번호 아님")

print("\n")
print('comprehension : 반복문 + 조건문 + 값 생성을 한 줄로 표현')
print("\n")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li = []
for i in a :
    if i % 2 == 0:
        li.append(i)
print(li)

print(list( i for i in a if i % 2 == 0))

dats = [1, 2, 'a', True, 3.0]
li2 = [ i * i for i in dats if type(i) == int]
print(li2)

id_name = {1 : 'tom', 2 : 'holland'}
name_id = {val:key for key, val in id_name.items()}
print(name_id)

print("\n")
print([1, 2, 3])
print(*[1, 2, 3]) # * : unpack

aa = [(1, 2), (3, 4), (5, 6)]
for a, b in aa :
    print(a + b)

print([a + b for a, b in aa], sep ='\n')
print(*[a + b for a, b in aa], sep ='\n')

print("\n")
print('수열 생성 : range')
print("\n")

print(list(range(1, 6))) #[]
print(tuple(range(1, 6, 2))) #()
print(list(range(-10, -100, -20)))
print(set(range(1, 6))) #{}
print("\n")
for i in range(6) :
    print(i, end = ' ')
print("\n")

for _ in range(6):
    print('반복')
print("\n")

tot = 0
for i in range(1, 11):
    tot += i
print('tot : ', tot)
print('tot : ', sum(range(1, 11)))

print("\n")

for i in range(1, 10) :
    print(f'2 * {i} = {2 * i}')

# 문1 : 2 ~ 9 구구단 출력 (단은 행 단위 출력) for 문 사용
for a in range(2, 10) :
    for b in range(1, 10) :
        print(f'{a} * {b} = {a * b}', end = ' ')
    print("\n")

# 문2 : 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
for i in range(6) :
    n1 = i + 1
for j in range(6) :
    n2 = j + 1
    n = n1 + n2
    if n % 4 == 0 :
        print(n1, n2)

print('\nend')