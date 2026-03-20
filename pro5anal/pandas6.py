import pandas as pd
import numpy as np

items = {
    'apple':{'count':10, 'price' : 1500},
    'orange':{'count':5, 'price' : 1000},
    }

df = pd.DataFrame(items)
print(df)

# DataFrame 저장
# 클립보드로 저장
df.to_clipboard()       # 메모장 등에 저장
print(df.to_html())
print(df.to_json())

df.to_csv('result1.csv', sep=',')
df.to_csv('result2.csv', sep=',', index=False)      # 이상적
df.to_csv('result3.csv', sep=',', index=False, header=False)
print()

df2 = df.T
print(df2)
df2.to_csv('result4.csv', sep=',', index=False, encoding='utf-8-sig')
redata = pd.read_csv('result4.csv')
print(redata)

print('\nExcel 관련 ---------')
df3 = pd.DataFrame({
    'name':['Alice', 'Bob', 'John'],
    'age':[24, 22, 23],
    'city':['seoul','suwon','incheon']
})
print(df3)

# Excel 파일 .i/o
# 저장
df3.to_excel('result.xlsx', index=False, sheet_name='work1')

# 읽기
exdf = pd.ExcelFile("result.xlsx")
print(exdf.sheet_names)
df4 = exdf.parse("work1")
print(df4)