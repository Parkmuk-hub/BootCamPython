# 문1 : 2 ~ 9 구구단 출력 (단은 행 단위 출력) for 문 사 용


for a in range(2, 10) :
    for b in range(1, 10) :
        print(f'{a} * {b} = {a * b}')
    print("\n")