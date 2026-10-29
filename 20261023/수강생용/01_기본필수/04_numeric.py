
import pandas as pd
from sklearn.preprocessing import StandardScaler

# 데이터 입력
train = pd.DataFrame({"input_chars": [100, 200, 300]})
valid = pd.DataFrame({"input_chars": [400, 500]})

# 데이터 편집 처리
scaler = StandardScaler()
scaler.fit(train)
valid_ready = scaler.transform(valid)

# 계산된 평균과 변환 결과 출력
print("train에서 배운 평균:", scaler.mean_.tolist())
print("valid 변환 결과:")
print(valid_ready.round(3))
