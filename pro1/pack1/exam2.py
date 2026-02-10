"""
반복문 for를 사용 : 1 ~ 100 사이의 숫자 중 3의 배수 또는 4의 배수 이고 7의 배수가 아닌 수를 출력하고 건수와 합도 출력하는 코드를 작성하시오
출력 결과
3 4 6 8 9 12 15 16 18 20 21 24 27 30 ...
건수 : ...
배수의 총합 : ...
"""
total = 0
count = 0

for i in range(1, 100, 1) :
    if i % 3 == 0 or i % 4 == 0 and i % 7 != 0 :
        print(i, end = ' ')
        total += i
        count += 1

print()
print("건수: ", count)
print("배수의 총합: ", total)