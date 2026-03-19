# 편차가 큰 데이터에 대한 로그 변환
# 따로 정리가 필요한 부분임

# ML(머신러닝)에서 데이터 분석 시 log를 사용하면?
# 1) scale(규모) 차이를 축소 ex : log(10) = 1, log(100) = 2, log(1000) = 4
# 2) 로그 변환하면 치우친 데이터를 정규분포에 가깝게 변경 가능
# 3) 모델링에서 지수 관계를 선형 관계로 바꿈 

import numpy as np
np.set_printoptions(suppress=True, precision=6)

def test() :
    values = np.array([345, 34.5, 3.45, 0.345, 0.01, 0.1, 10, 100])
    print(np.log2(3.45), ' ', np.log10(3.45), ' ', np.log(3.45))

    print("원본 값 : ", values)
    log_values = np.log10(values)
    print('상용 로그 : ', log_values)
    ln_values = np.log(values)
    print('자연 로그 : ', ln_values)

    # 정규화 : 모든 데이터를 0 ~ 1사의 범위 내에서 표시
    min_log = np.min(log_values)
    max_log = np.max(log_values)
    normalized = (log_values - min_log) / (max_log - min_log)
    print("정규화 결과 : ", normalized)

class LogTrans :
    # 편차가 큰 데이터를 로그 스케일 변환하고 그 역변환을 제공하는 클래스
    def __init__(self, offset:float=1.0):       # 0 이나 음수 피하기위한 offset
        self.offset = offset

    # 로그 변환 메소드
    def transForm(self, x:np.ndarray) -> np.ndarray :       # 가독성을 위해 type 힌트
        return np.log(x + self.offset)
    
    # 역변환 메소드
    def inverse_trans(self, x_log:np.ndarray) -> np.ndarray:
        return np.exp(x_log) - self.offset 
    

def main() :
    test()
    print('***' * 10)
    data = np.array([0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000], dtype=float)

    log_trans = LogTrans(offset=1.0)
    data_log_scaled = log_trans.transForm(data)     # 로그 변환
    reversed_data = log_trans.inverse_trans(data_log_scaled)

    print("원본 : ", data)
    print("로그 변환 : ", data_log_scaled)
    print("역변환 : ", reversed_data)

if __name__ == "__main__" :
    main()