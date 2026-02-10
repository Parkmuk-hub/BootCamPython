# 문2 : 주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 출력
for a in range (1, 7) :
    for b in range(1, 7):
        sum = int(a + b)
        if sum % 4 == 0:
            print(f'{a}, {b}')
        else :
            pass