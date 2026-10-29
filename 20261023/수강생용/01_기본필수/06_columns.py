
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# 데이터 입력
train = pd.DataFrame({"input_chars": [100, 200, 300],
                      "task_type": ["qa", "summary", "qa"]})
valid = pd.DataFrame({"input_chars": [400, 500],
                      "task_type": ["summary", "qa"]})

# 데이터 변환 및 처리
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), ["input_chars"]),
    ("cat", OneHotEncoder(sparse_output=False), ["task_type"]),
])
preprocessor.fit(train)
valid_ready = preprocessor.transform(valid)

# 변환 전후 결과 확인
print("변환 전:", valid.shape)
print("변환 후:", valid_ready.shape)
print(valid_ready.round(3))
