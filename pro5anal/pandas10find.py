# BeautifulSoup 객체 메소드 활용
from bs4 import BeautifulSoup

html_page = """
<html><body>
<h1>제목 태그</h1>
<p>웹 문서 연습</p>
<p>원하는 자료 확인</p>
</body></html>
"""
print(type(html_page))      # <class 'str'>
soup = BeautifulSoup(html_page, 'html.parser')
print(type(soup))       # <class 'bs4.BeautifulSoup'>
print()

h1 = soup.html.body.h1
print("h1 : ", h1.string)       # h1 :  제목 태그
print("h1 : ", h1.text)
print()

p1 = soup.html.body.p   # 최초의 p
print("p1 : ", p1.string)       # p1 :  웹 문서 연습
print()

p2 = p1.next_sibling.next_sibling       # DOM을 이용한 자료 접근
print("p2 : ", p2.string)       # p2 :  원하는 자료 확인
print()

print('\n-- find() method 활용------')
html_page2 = """
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹 문서 연습</p>
<p id="my" class="our">원하는 자료 확인</p>
</body></html>
"""
soup2 = BeautifulSoup(html_page2, 'html.parser')
# find(tag명, attrs, recursive, string)     # <p>웹 문서 연습</p>, 웹 문서 연습
print(soup2.p, ' ', soup2.p.string)
print(soup2.find('p').string)               # 웹 문서 연습
print(soup2.find('p', id="my").string)      # 원하는 자료 확인 / find(id="my"), find(attrs={"id":"my"})도 같은 값
print(soup2.find(id="title").string)        # 제목 태그
print(soup2.find(class_="our").string)      # 원하는 자료 확인 
print(soup2.find(attrs={"class":"our"}).string)     # 원하는 자료 확인
print(soup2.find(attrs={"id":"my"}).string)
print()

print('\n-- find_all(), findAll() method 활용------')
html_page3 = """
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹 문서 연습</p>
<p id="my" class="our">원하는 자료 확인</p>
<div>
    <a href="https://www.naver.com">네이버</a>
    <a href="https://www.daum.net">다음</a>
</div>
</body></html>
"""
soup3 = BeautifulSoup(html_page3, 'html.parser')
print(soup3.find_all(['a']))
print(soup3.find_all(['a','p']))
print()

links = soup3.find_all('a') # [<a href="https://www.naver.com">네이버</a>, <a href="https://www.daum.net">다음</a>]
# print(links)
for i in links :
    href = i.attrs["href"]
    text = i.text
    print(href, " ", text)      # https://www.naver.com   네이버 \n https://www.daum.net   다음

print('\n정규표현식 사용----')
import re
link2 = soup3.find_all(href=re.compile(r'^https'))  # [<a href="https://www.naver.com">네이버</a>, <a href="https://www.daum.net">다음</a>
# print(link2)
for k in link2 :
    print(k.attrs['href'])      # https://www.naver.com \n https://www.daum.net

print('\n-----bugs 사이트 음악 순위 읽기')
import requests
url = "https://music.bugs.co.kr/chart"
response = requests.get(url)
bsoup = BeautifulSoup(response.text, 'html.parser')
musics = bsoup.find_all("td", class_="check")
for idx, music in enumerate(musics):
    print(f"{idx + 1}위) {music.input['title']}")



