"""실습 03: 여러 트리를 결합하는 Random Forest를 실행합니다."""
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

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

# RandimFirest를 이용하여 train으로 훈련하고 valid 예측, 출력
model = RandomForestClassifier(n_estimators=20, max_depth=3, random_state=42, n_jobs=1)
model.fit(X_train, y_train)
prediction = model.predict(X_valid)
print("트리 수:", len(model.estimators_))
print("valid 예측:", prediction.tolist())
print("valid F1:", round(f1_score(y_valid, prediction, zero_division=0), 3))
