"""실습 04: 2 → 8 → 2 신경망의 순전파를 확인합니다."""
import torch
from torch import nn

# 난수 시드 고정
torch.manual_seed(42)

# 인공 신경망 형성 
model = nn.Sequential(nn.Linear(2, 8), nn.ReLU(), nn.Linear(8, 2))

# 데이터 입력
X = torch.tensor([[1.0, 2.0], [3.0, 4.0], [0.0, 1.0], [2.0, 0.0]])
logits = model(X)

# 결과 출력
print("입력:", tuple(X.shape))
print("출력:", tuple(logits.shape))
print("파라미터 수:", sum(p.numel() for p in model.parameters()))
