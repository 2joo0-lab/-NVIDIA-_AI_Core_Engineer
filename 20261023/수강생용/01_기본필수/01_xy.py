from pathlib import Path
import pandas as pd


# CSV 파일 데이터 읽기
HERE = Path(__file__).resolve().parent
data = pd.read_csv(HERE / "requests.csv")

# X,y 데이터 입력
X = data[["input_chars", "task_type"]]
y = data["failed"]

# 입력값 및 모양, 정답 출력 
print("입력 열:", X.columns.tolist())
print("X 모양:", X.shape)
print("y 모양:", y.shape)
print("처음 3개 정답:", y.head(3).tolist())
