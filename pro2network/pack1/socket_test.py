# socket이란? TCP/TP의 프로그래머 인터페이스이다.
# 네트워크로 연결된 두 컴퓨터(서버-클라이언트) 간에 실시간 양방향 데이터 송수신을 가능하게 하는 기술입니다. 
# 파이썬의 socket 모듈을 사용해 TCP/IP 기반의 안정적인 연결을 생성하고, 
# 데이터를 주고받거나 연결을 끊는 등 네트워크 프로그래밍의 기초가 됩니다. 
# 통신 기기간 대화가 가능하도록 하는 통신방식으로 클라이언트/서버 모델에 기초한다.
# 연결지향 : TCP/IP
# 비연결지향 :

# socket 통신 확인
import socket

print(socket.getservbyname('http', 'tcp'))  # www 환경 전송규약
print(socket.getservbyname('ssh', 'tcp'))   #  원격 컴 접속
print(socket.getservbyname('ftp', 'tcp'))   # 파일 전송
print(socket.getservbyname('smtp', 'tcp'))  # 메일 송수신
print(socket.getservbyname('pop3', 'tcp'))  # 이메일
print()
# 특정 웹 서버의 ipaddress 확인
print(socket.getaddrinfo('www.daum.net', 80, proto=socket.SOL_TCP))
print()
print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))




