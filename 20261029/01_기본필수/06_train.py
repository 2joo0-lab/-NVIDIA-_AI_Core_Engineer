"""실습 06: 작은 정상 자료로 학습 순서만 익힙니다. 여기는 train 오차 확인용입니다."""
import torch
from torch import nn

# 데이터 입력
torch.manual_seed(42) # 난수 시드 고정
X = torch.tensor([[-2., -1.], [-1., -1.], [-1., 0.], [0., -1.],
                  [1., 0.], [0., 1.], [1., 1.], [2., 1.]])
y = torch.tensor([0, 0, 0, 0, 1, 1, 1, 1], dtype=torch.long)

# ANN(인공신경망) 형성
model = nn.Sequential(nn.Linear(2, 8), nn.ReLU(), nn.Linear(8, 2))

# 모델의 점수와 정답을 비교해 손실 계산
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.1) # 손실 줄이기 위해 모델 파라미터 갱신
print("학습 전 loss:", round(loss_fn(model(X), y).item(), 6)) # 학습 전 손실 체크

# 모델 반복 학습
model.train()
for epoch in range(80):
    optimizer.zero_grad()           # 1. 기울기 초기화
    loss = loss_fn(model(X), y)     # 2. 순전파 및 손실 계산
    loss.backward()                 # 3. 역전파(미분-기울기 계산)
    optimizer.step()                # 4. 파라미터 갱신

# 학습 후 결과 확인
model.eval() # 평가모드로 전환
with torch.no_grad(): # 기울기 계산 X
    logits = model(X) # 학습한 모델로 다시 계산
    print("학습 후 loss:", round(loss_fn(logits, y).item(), 6))
    print("train 정확도:", round((logits.argmax(dim=1) == y).float().mean().item(), 4))
print("주의: 위 정확도는 학습한 8건의 결과이며 새로운 자료의 성능이 아닙니다.")
