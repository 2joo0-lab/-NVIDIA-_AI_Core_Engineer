"""실습 06: train 12건 안에서만 3-fold 교차검증합니다."""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

# 현재 파일이 있는 폴더에서 requests.csv 파일을 불러와 읽습니다
HERE = Path(__file__).resolve().parent
raw = pd.read_csv(HERE / "requests.csv")

# 읽어 온 데이터를 분류하여 저장
develop, test = train_test_split(raw, test_size=0.2, stratify=raw["failed"], random_state=42)
train, valid = train_test_split(develop, test_size=0.25, stratify=develop["failed"], random_state=42)
# test 4건은 보관만 합니다. 입력은 실행 전에 아는 글자 수입니다.
X_train = train[["input_chars"]]
X_valid = valid[["input_chars"]]
y_train = train["failed"]
y_valid = valid["failed"]

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score

# 데이터를 3개 묶음으로 나누고 DecisionTree모델으로 교차검증
folds = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
scores = cross_val_score(model, X_train, y_train, cv=folds, scoring="f1") #X_train과 y_train만 사용해 세 번 학습·검증하고, 각 검증 점수를 scores에 저장합니다.
print("fold별 F1:", scores.round(3).tolist())
print("평균 F1:", round(scores.mean(), 3))
print("표준편차:", round(scores.std(), 3))
