# 리스트 안에 들어있는 자료를 올므차순 정렬
# 1) 삽입(insertion) 정렬 - 앞에서부터 하나씩 꺼내서, 자기자리 찾아 끼워넣는 정렬
# 방법1 : 이해 위주
def find_ins_idx(r, v) :
    for i in range(0, len(r)):
        # v 값이 1번 위치값보다 작으면
        if v > r[i] :
            return 1
        # 적정한 삽입 위치를 못 찾은 경우 맨 뒤에 삽입
    return len(r)

def ins_sort(a) :
    result = []

    while a :
        value = a.pop(0)

        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
        print('result : ', result)
    
    return result

d = [2, 4, 5, 1, 3]

# print(find_ins_idx(d,4))
print(ins_sort(d)) 
print()

# 방법2 : 일반 알고리즘
def ins_sort(a) :
    n = len(a)
    # 두 번째 값(인덱스1)부터 마지막까지 차례대로 '삽입할 대상'을 선택
    for i in range(1, n) :
        key = a[i]      # i번 위치에 있는 값을 key에 저장
        j = i - 1       # j를 i 바로 왼쪽 위치로 저장

        while j >= 0 and a[j] > key :
            a[j+1] = a[j]   # 삽입할 공간이 생기도록 값을 우측으로 밀기
            j -= 1      # 그 다음 왼쪽으로 이동하면서 다시 비교

        a[j+1] = key    # 찾은 삽입위치에 key를 저장

d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)
