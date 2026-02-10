# 예외처리 : 파일, 네트워크, DB작업, 실행에러 등의 에러 대처

def divide(a, b):
    return a / b
print("이런 저런 작업 진행-------")

#c = divide(5, 2)
#print(c)

try :
    # 실행문(예외 발생 가능 구문)
    #c = divide(5, 0)
    #print(c)

    #aa = [1, 2]
    #print(aa[0])
    #print(aa[2])
    open("c:/work/abc.txt")
except ZeroDivisionError : # 예외, 종류 관련 클래스
    print('두 번째 값은 0을 주면 안됨') # 예외 발생 처리 구문
except IndexError as e : # as 변수를 설정해주면 더 자세한 내용을 알 수 있음
    print("참조 범위 오류 : ", e)
except Exception as a : # 얘가 에러 잡는 것 중 상위
    print("에러 :", a)

finally :
    print("에러 유무에 상관없이 반드시 수행한다.")

print('end')
print('종료')



"""
에러 별 처리는 지양
Exception as 변수로 에러들 모두 처리
이제 곧 파일, DB작업 START
"""