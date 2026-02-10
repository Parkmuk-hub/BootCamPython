# 조건 판단문 if
var = 5

if var >= 3 :
    print('크네') # 조건식이 틀리면 실행 안함

if var <= 3 :
    print('작구나')
else:
    print('크구나')

print()

money = 200
age = 35
if money >= 500:
    item = '사과'
    if age <= 30:
        msg = "참 참"
    else: 
        msg = "참 거짓"
else:
    item = '청사과'
    if age >= 20:
        msg = "거짓 참"
    else: 
        msg = "거짓 거짓"

print(f'중복 if 수행 후 결과 : {item} {msg}')

print()

#data = input('점수 : ') # 입력 받은 값은 모두 문자열
#score = int(data) # 무조건 정수로 바꿔줘야함
score = 80
if score >= 90 :
    print('우수')
elif score >= 80 :
    print('보통')
else :
    print('과락')

jumsu = 80
if 90 <= jumsu <= 100 :
    print('A')
elif 70 <= jumsu < 90 :
    print("B")
else :
    print("F")

print('__________________________________________________',"\n")
names = ['홍길동', '신선해', '이기자']
if '홍길동' in names :
    print('친구 이름이야')
else :
    print('누구임?')


if(count := len(names)) >= 3: # <- 대입 표현식 count : count = len(names)
    print(f"인원 수가 { count}명이므로 단체할인 '적용'")
else :
    print("아쉽네")

total = [ 95, 88, 76, 92, 81]
if ( avg := sum(total)/len(total)) >= 80 :
    print(f"우수반 : 평균점수{avg}")
else :
    print(f"멍청한 반 : 평균점수{avg}")

print()
print('삼항 연산')
a = 'kbs'
b = 9 if  a == 'kbs' else 11 # ''안에 띄어쓰기 조심
print('b :', b)

a = 11
b = 'tvn' if a == 19 else 'sbs' # if문은 하나만 사용하는 것을 추천, 이중 if문은 가독성이 떨어짐
print('b :', b)

a = 3
if a < 5:
    print(0)
elif a < 10 :
    print(1)
else :
    print(2)

print(0 if a < 5 else 1 if a < 10 else 2)

print('end') # 조건식이랑 상관 없음

