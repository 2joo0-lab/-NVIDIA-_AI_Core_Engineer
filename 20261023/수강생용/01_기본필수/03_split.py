
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

# csv 파일 데이터 읽기
HERE = Path(__file__).resolve().parent
data = pd.read_csv(HERE / "requests.csv")

# test, valid, train 데이터 분리
test_ratio = 0.2
train_valid, test = train_test_split(
    data, test_size=test_ratio, random_state=42, stratify=data["failed"])
train, valid = train_test_split(
    train_valid, test_size=0.25, random_state=42, stratify=train_valid["failed"])

# 분류한 데이터 확인
print("train:", len(train))
print("valid:", len(valid))
print("test:", len(test))
print("valid ID:", valid["request_id"].tolist())
print("test는 오늘 학습과 예측에 사용하지 않습니다.")
