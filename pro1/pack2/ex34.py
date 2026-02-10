print("파일 처리 ------------")
import os

try:
    print(os.getcwd()) # C:\work\projects\pro1\pack2
    #f1 = open(os.getcwd() + r"C:\work\projects\pro1\pack2\ftext.txt", encoding='utf-8')
    #f1 = open(os.getcwd() + r"\ftext.txt", encoding='utf-8')
    #f1 = open("ftextt.txt", encoding='utf-8')
    f1 = open("ftext.txt", mode = 'r', encoding='utf-8') # mode = 'r', 'w', 'a', 'b' ...
    print(f1)
    print(f1.read())

    print("파일 저장 -------")
    f3 = open("ftext2.txt", mode = "w", encoding='utf-8')
    f3.write('내 친구들 \n')
    f3.write('고길동, 한국인')
    f3.close()
    print('파일 저장 성공')

    f3 = open("ftext2.txt", mode = 'a', encoding='utf-8')

    f3.write("\사오정")
    f3.write("\저팔계")
    f3.write("\손오공")
    f3.close()
    print("파일 추가 성공")

except Exception as e :
    print('파일 처리 오류: ', e)
