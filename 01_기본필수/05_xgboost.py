"""실습 05: XGBoost도 같은 fit·predict 흐름으로 실행합니다."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

# 현재 파일이 있는 폴더에서 requests.csv 파일을 불러와 읽습니다.
HERE = Path(__file__).resolve().parent
raw = pd.read_csv(HERE / "requests.csv")

# 읽어 온 데이터를 분류하여 저장
develop, test = train_test_split(raw, test_size=0.2, stratify=raw["failed"], random_state=42)
train, valid = train_test_split(develop, test_size=0.25, stratify=develop["failed"], random_state=42)
X_train = train[["input_chars"]]
X_valid = valid[["input_chars"]]
y_train = train["failed"]
y_valid = valid["failed"]

from xgboost import XGBClassifier
from sklearn.metrics import f1_score

# 학습 회차 80·깊이 2·보정 크기 0.05를 고정합니다. CPU로 실행합니다.
model = XGBClassifier(n_estimators=80, max_depth=2, learning_rate=0.05,
                      objective="binary:logistic", eval_metric="logloss",
                      tree_method="hist", random_state=42, n_jobs=1)
# train으로 학습 및 valid 예측.
model.fit(X_train, y_train)
prediction = model.predict(X_valid)

# 결과값 출력
print("valid 예측:", prediction.tolist())
print("valid F1:", round(f1_score(y_valid, prediction, zero_division=0), 3))
print("학습 목적: 실패 분류 / 확인 지표: F1")
