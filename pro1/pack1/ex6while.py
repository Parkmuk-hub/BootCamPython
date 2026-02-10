# while 기본문
a = 1 

while a <= 5 :
    print(a, end = '\n')
    # a = 6
    a += 1 # 5를 찍으면 멈춤 
    #break  #안쓰면 무한 반복함 ctrl + c 하면 멈춤
else :
    print('수행 성공') # 알맞게 실행하면 이 문장을 출력하고 break를 만나면 출력 안함

# 이중 while문
print('__________________________________________________',"\n")

i = 1

while i <= 3 :  
    j = 1
    while j <= 4 : 
        print('i = ' + str(i) + ' ' + 'j = ' + str(j))
        j += 1
    i += 1

print('__________________________________________________',"\n")
print('1 ~ 100 사이 정수 중 3의 배수의 합')
s = 1
total = 0
while s <= 100 :
    if s % 3 == 0 :
        total += s
    s += 1

print(('합은 : '), total)

print('__________________________________________________',"\n")

colors = ["빨강", "노랑", "보라"] # 배열의 첫 번째 요소와 인덱스 0번은 빨강
num = 0
#print(colors[num])
#print(colors[1])
#print(colors[2])
while num < len(colors) : # 직접 세지말고 len(변수 이름) 하여 편하게 쓰자
    print(colors[num])
    num += 1

print('__________________________________________________',"\n")
print('별 찍기 ')
k = 1
while k <= 10 :
    m = 1
    msg = ''
    while m <= k :
        msg += "*"
        m += 1
    print(msg)
    k += 1
print('__________________________________________________',"\n")
print('if 블럭 내 while 블럭 사용 ')
""""
import time
sw = input("폭탄 스위치를 누를까요? [y/n] ")
if sw == 'Y' or sw == 'y' :
    count = 5
    while 1 <= count :
        print('%d초 남았습니다.' %count)
        time.sleep(1)
        count -= 1
    print("Boom!")
elif sw == 'N' or sw == 'n' :
    print('작업 취소')
else :
    print('다시 입력하세요.')
"""
print('__________________________________________________',"\n")
print('continue와 break ')

p = 0
while p < 10 :
    p += 1
    if p == 3 : continue # 아래 문장을 무시하고 while로 이동 
    if p == 5 : continue # 아래 문장을 무시하고 while로 이동 
    #if p == 7 : break # while 문 탈출

    print(p)
else :
    print("정상 종료")

print("while 문 실행 후 %d" %p)

print('__________________________________________________',"\n")
print(' 키보드로 숫자를 입력받아 홀수 짝수 확인하기 (무한 반복)')

while True : # 아래 문장이 False가 될 때까지 무한 반복
    sm = input("정수를 입력하세요 :")
    sm = int(sm)
    if sm == 0 :
        print('종료합니다.')
        break
    elif sm % 2 == 0 :
        print("%d은(는) 짝수입니다." %sm)
    elif sm % 2 == 1 : 
        print("%d은(는) 홀수입니다." %sm)
print('end')

