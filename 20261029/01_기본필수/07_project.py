"""실습 07~08: 정상 데이터 20건. train 12건 학습, valid 4건 확인, test 4건 보관."""
from pathlib import Path
import csv
import json
import torch
from torch import nn

# csv 파일 불러와 읽기
base = Path(__file__).resolve().parent
with (base / "points.csv").open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

# 데이터 지정
train_rows = [r for r in rows if r["split"] == "train"]
valid_rows = [r for r in rows if r["split"] == "valid"]
X_train = torch.tensor([[float(r["x1"]), float(r["x2"])] for r in train_rows])  # 입력 텐서 (학습용)
y_train = torch.tensor([int(r["label"]) for r in train_rows], dtype=torch.long) # 정답 텐서 (학습용)
X_valid = torch.tensor([[float(r["x1"]), float(r["x2"])] for r in valid_rows])  # 입력 텐서 (검증용)
y_valid = torch.tensor([int(r["label"]) for r in valid_rows], dtype=torch.long) # 정답 텐서 (학습용)

#
torch.manual_seed(42) # 난수 시드 고정
model = nn.Sequential(nn.Linear(2, 8), nn.ReLU(), nn.Linear(8, 2)) #ANN(인공 신경망) 형성
loss_fn = nn.CrossEntropyLoss() # 손실 계산
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)  # 파라미터 갱신
history = [[0, loss_fn(model(X_train), y_train).item()]] # 학습 전 손실

# 모델 반복 학습
model.train()
for epoch in range(1, 81):
    optimizer.zero_grad()                    # 1. 기울기 초기화
    loss = loss_fn(model(X_train), y_train)  # 2. 순전파 및 손실 계산  
    loss.backward()                          # 3. 역전파(미분-기울기 계산)
    optimizer.step()                         # 4. 파라미터 갱신
    
    # 갱신 후 같은 train 자료의 loss를 기록합니다. 마지막 batch loss와 구분합니다.
    with torch.no_grad():
        history.append([epoch, loss_fn(model(X_train), y_train).item()])

# 데이터 검증 및 예측
model.eval()                                                     # 평가 모드로 전환
with torch.no_grad():                                            # 기울기 계산 X
    logits = model(X_valid)                                      # 검증 데이터 입력
    prediction = logits.argmax(dim=1)                            # 가장 높은 logit 열 번호 예측
    accuracy = (prediction == y_valid).float().mean().item()     # 예측값과 정답 비교하여 정확도 계산

# 계산 결과 파일로 저장
with (base / "training_history.csv").open("w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["epoch", "train_loss_eval"])
    writer.writerows(history)
# 딕셔너리로 정리    
metrics = {"device": "cpu", "epochs": 80, "train_rows": 12, "valid_rows": 4,
           "test_used": False, "valid_accuracy": accuracy,
           "initial_train_loss": history[0][1], "final_train_loss": history[-1][1],
           "valid_ids": [r["id"] for r in valid_rows], "actual": y_valid.tolist(),
           "predicted": prediction.tolist()}
# json으로 바꿔 저장
(base / "final_metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8") 
(base / "gpu_check.txt").write_text(
    f"torch={torch.__version__}\ncuda_build={torch.version.cuda}\n"
    f"cuda_available={torch.cuda.is_available()}\nselected_device=cpu\n", encoding="utf-8")

# 결과값 출력
print("분할: train 12 / valid 4 / test 4(보관)")
print("train loss:", round(history[0][1], 6), "->", round(history[-1][1], 6))
print("valid 정확도:", round(accuracy, 4))
print("valid 예측:", prediction.tolist())
print("생성: gpu_check.txt, training_history.csv, final_metrics.json")
