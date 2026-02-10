import re # 정규 표현식 지원 모듈 로딩

ss = "1234 abc가나다abcABC_123555_6집에가나요'Python No Jam'"
print(ss)
print(re.findall(r'123', ss)) # 정규 표현할 때 r을 선행하라
# findall의 리턴 값은 list
print(re.findall(r'가나', ss))
print(re.findall(r'[0-9]', ss))
print(re.findall(r'[0-9]+', ss))
print(re.findall(r'[0-9]*', ss))
print(re.findall(r'[0-9]?', ss))
print(re.findall(r'[0-9]{2}', ss))
print(re.findall(r'[0-9]{2,3}', ss))
print(re.findall(r'[a-zA-z]', ss))
print(re.findall(r'[a-zA-z]+', ss))
print(re.findall(r'[가-핳]', ss))
print(re.findall(r'[가-핳]+', ss))
print(re.findall(r'\d+', ss))











