import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

# 출력 인코딩 설정
sys.stdout.reconfigure(encoding="utf-8")

# 1. 페이지 주소들을 리스트로 준비
urls = [
    "https://finance.naver.com/sise/sise_market_sum.naver?&page=1",
    "https://finance.naver.com/sise/sise_market_sum.naver?&page=2"
]
headers = {"User-Agent": "Mozilla/5.0"}
results = [] # 모든 페이지의 데이터를 담을 큰 바구니

# 2. 반복문을 통해 각 페이지 방문
for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # 3. 데이터 추출 (해당 페이지의 줄들 찾기)
    rows = soup.select("table.type_2 > tbody > tr")
    
    for r in rows:
        table = r.find_all("td")
        if len(table) > 1:
            name = table[1].get_text(strip=True)  # 종목명
            siga = table[6].get_text(strip=True)  # 시가총액
            # 바구니(results)에 차곡차곡 쌓기 (1페이지 + 2페이지 데이터가 합쳐짐)
            results.append({"종목명": name, "시가총액": siga})

# 4. 데이터프레임 생성 및 CSV 저장
kosp = pd.DataFrame(results)
kosp.to_csv("kosp.csv", index=False, encoding="utf-8-sig")

# 5. 확인을 위해 읽어오기
df_read = pd.read_csv("kosp.csv")
print("--- [수집 완료] 전체 데이터 중 상위 5개 ---")
print(df_read.head(5))
print(f"총 수집된 종목 수: {len(df_read)}개")