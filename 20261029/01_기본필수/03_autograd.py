"""실습 03: x=3에서 y=x²+2x+1과 기울기를 계산합니다."""
import torch

# 값이 3.0인 텐서를 만들고, requires_grad=True로 설정해 x에 대한 미분을 추적하도록 합니다.
x = torch.tensor(3.0, requires_grad=True)
y = x**2 + 2*x + 1
# <<< B03
# backward는 y 값을 바꾸지 않고 x.grad에 기울기를 계산합니다.
y.backward()
print("y:", y.item())
print("dy/dx:", x.grad.item())
