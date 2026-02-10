i=10
while i >= 1 :
    j = 10
    while j > 0:
        if j > i:
            print(" ", end='')
        else:
            print("*", end='')
        j-=1
    print()
    i -= 1