"""실습 05: 정답 인덱스와 logits로 손실을 계산합니다."""
import torch
from torch import nn

# 데이터 입력
logits = torch.tensor([[2.0, 0.0], [0.0, 2.0]])
target = torch.tensor([0, 1], dtype=torch.long)

# 분류 손실 검사
loss_fn = nn.CrossEntropyLoss()
loss = loss_fn(logits, target)

# 결과 츨력
print("logits:", tuple(logits.shape))
print("target:", tuple(target.shape), target.dtype)
print("loss:", round(loss.item(), 6))
