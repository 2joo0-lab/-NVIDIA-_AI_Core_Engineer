
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier


# CSV 파일 데이터 읽기
HERE = Path(__file__).resolve().parent
data = pd.read_csv(HERE / "requests.csv")

# test, valid, train 데이터 분리
train_valid, test = train_test_split(
    data, test_size=0.2, random_state=42, stratify=data["failed"])
train, valid = train_test_split(
    train_valid, test_size=0.25, random_state=42, stratify=train_valid["failed"])

# 입력 특성과 정답 선택
features = ["input_chars", "task_type"]
X_train = train[features]
y_train = train["failed"]
X_valid = valid[features]

# 숫자 열과 범주 열에 맞는 전처리 준비
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), ["input_chars"]),
    ("cat", OneHotEncoder(sparse_output=False), ["task_type"]),
])

# 전처리와 기준 모델을 하나의 파이프라인으로 연결
pipeline = Pipeline([("pre", preprocessor),
                     ("model", DummyClassifier(strategy="most_frequent"))])

# train으로 전처리 기준과 모델 학습
pipeline.fit(X_train, y_train)

# valid 입력으로 실패 여부 예측
prediction = pipeline.predict(X_valid)

# 실제 정답과 예측값을 정리해 CSV로 저장
result = valid[["request_id", "failed"]].copy()
result["predicted"] = prediction
result.to_csv(HERE / "valid_predictions.csv", index=False, encoding="utf-8-sig")

# 검증 정확도와 결과 출력 (test는 사용하지 않음)
accuracy = (result["failed"] == result["predicted"]).mean()
print("분할:", len(train), len(valid), len(test))
print(result.to_string(index=False))
print("valid 정확도:", round(accuracy, 2))
print("저장: valid_predictions.csv / test는 사용하지 않았습니다.")
