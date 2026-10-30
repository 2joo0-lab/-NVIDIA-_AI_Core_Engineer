from pathlib import Path
import pandas as pd
import torch
from torch import nn

torch.set_num_threads(1) # CPU 스레드 수 고정
base = Path(__file__).resolve().parent # 현재 폴더 경로 지정

import matplotlib
matplotlib.use("Agg")  # 창을 띄우지 않고 PNG에 저장합니다.
import matplotlib.pyplot as plt

# csv 파일을 불러와 읽고 데이터를 분류하여 저장
df = pd.read_csv(base / "points.csv")
train = df[df["split"] == "train"]
valid = df[df["split"] == "valid"]
X_train = torch.tensor(train[["x1", "x2"]].values, dtype=torch.float32)
y_train = torch.tensor(train["label"].values, dtype=torch.long)
X_valid = torch.tensor(valid[["x1", "x2"]].values, dtype=torch.float32)
y_valid = torch.tensor(valid["label"].values, dtype=torch.long)

loss_fn = nn.CrossEntropyLoss() # 손실 계산 함수
summary = [] # 결과 저장용 빈 리스트

# 학습 모델(인공신경망) 구축 및 데이터 학습
for name, lr in [("baseline", 0.001), ("candidate", 0.01)]:
    torch.manual_seed(42) # 난수 시드 고정
    model = nn.Sequential(nn.Linear(2, 8), nn.ReLU(), nn.Linear(8, 2)) # 신경망 구성
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=0.0) # AdamW 방식 사용
    history = []
    for epoch in range(1, 21):                      # epoch 20회
        model.train()                               # 모델 학습
        optimizer.zero_grad()                       # 기울기 초기화
        loss = loss_fn(model(X_train), y_train)     # 순전파 - 손실 계산
        loss.backward()                             # 역전파 - 기울기 계산
        optimizer.step()                            # 파라미터 갱신

        model.eval()            # 평가 모드로 전환
        with torch.no_grad():   # 기울기 계산 X
            train_loss = loss_fn(model(X_train), y_train).item()
            valid_loss = loss_fn(model(X_valid), y_valid).item()
        history.append([epoch, train_loss, valid_loss])

    # 학습 결과 저장
    table = pd.DataFrame(history, columns=["epoch", "train_loss_eval", "valid_loss"])
    table.to_csv(base / f"history_{name}.csv", index=False)
    best = table.loc[table["valid_loss"].idxmin()]
    summary.append([name, lr, int(best["epoch"]), best["valid_loss"]])
    plt.figure(figsize=(8, 5))
    plt.plot(table["epoch"], table["train_loss_eval"], label="train (eval mode)")
    plt.plot(table["epoch"], table["valid_loss"], label="valid")
    plt.axvline(best["epoch"], linestyle="--", label="best epoch")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.tight_layout()
    plt.savefig(base / f"curves_{name}.png", dpi=150)
    plt.close()
result = pd.DataFrame(summary, columns=["setting", "lr", "best_epoch", "best_valid_loss"])
result.to_csv(base / "experiment_table.csv", index=False)

# 결과 출력
print(result.round(6).to_string(index=False))
print("test 미사용 / best epoch는 관찰한 최소 지점, 기본필수에서는 모델 저장·복원하지 않음")
