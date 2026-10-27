"""실습 02: 깊이만 바꾸고 같은 train·valid에서 비교합니다."""
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

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score

# DecisionTree로 반복 학습하여 예측
for depth in [1, 3]:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    train_f1 = f1_score(y_train, model.predict(X_train), zero_division=0)
    valid_f1 = f1_score(y_valid, model.predict(X_valid), zero_division=0)
    print(f"깊이 {depth}: train F1={train_f1:.3f}, valid F1={valid_f1:.3f}")
