# 문1) 1 ~ 100 사이의 정수 중 3의 배수나 2의 배수가 아닌 수를 출력하고, 합을 출력
print("\n",'1번 문제__________________________________________________',"\n")

sum = 0

for i in range(1, 101, 1) :
    if i % 2 != 0 or i % 3 == 0 :
        print(f'{i}')
        sum += i 

    else :
        pass

print('합 :', sum)

    
#문2) 2 ~ 5 까지의 구구단 출력
print("\n",'2번 문제__________________________________________________',"\n")
for i in range(2, 6, 1):
    for j in range(1, 10 ,1):
        print(f'{i} * {j} = {i * j}')
    print("\n")
#문3) 1 ~ 100 사이의 정수 중 “짝수는 더하고, 홀수는 빼서” 최종 결과 출력
print("\n",'3번 문제__________________________________________________',"\n")
total = 0
for z in range(1, 101, 1) :
    if z % 2 == 0 :
        total += z
    elif z % 2 != 0:
        total -= z
print(total)
#문4) -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력
print("\n",'4번 문제__________________________________________________',"\n")
to = 0
su = 0
for m in range(1, 100, 4):
    to += m
    if m == 97 :
        to *= -1

for n in range(3, 100, 4):
    su += n
print('to의 값 :', to)
print('su의 값 :', su)
sut = su + to
print('총합 :', sut)

#문5) 1 ~ 100 사이의 숫자 중 각 자리 수의 합이 10 이상인 수만 출력
print("\n",'5번 문제__________________________________________________',"\n")
i = 1
while i <= 10 :
    for j in range (0, 10, 1):
        tott = i + j
        if tott >= 10 :
            print(f'{i} + {j} = {tott}')
            if i == 10 and j == 0:
                break
        else :
            pass
    i += 1
#문6) 1부터 시작해서 누적합이 처음으로 1000을 넘는 순간의 숫자와 그때의 합을 출력
print("\n",'6번 문제__________________________________________________',"\n")

i = 1

while i >= 1 :
    z += i
    i += 1
    if z >= 1000 :
        print('1000을 넘긴 숫자 :', i)
        print('총합 :', z)
        break
    else :
        pass
    
#문7) 구구단을 출력하되 결과가 30을 넘으면 해당 단 중단하고 다음 단으로 이동
print("\n",'7번 문제__________________________________________________',"\n")

i = 1

while i <=9 :
    for z in range (1, 10, 1):
        print(f'{i} * {z} = {i * z}')
        if i * z > 30 :
            break
        else :
            pass
    i += 1
#문8) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
print("\n",'8번 문제__________________________________________________',"\n")

num = 2
count = 0

while num <= 1000 :
    i = 2
    ok = True 

    while i * i <= num :
        if num % i == 0:
            ok = False
            break
        i += 1
    if ok :
        print(num, end = " ")
        count += 1
    num += 1
print("\n")
print('소수 총합 : ', count)



