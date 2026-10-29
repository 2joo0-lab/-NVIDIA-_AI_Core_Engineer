"""실습 02: 값뿐 아니라 shape·dtype·device를 같이 확인합니다."""
import torch

# 텐서값 지정
scalar = torch.tensor(3.0)
vector = torch.tensor([1.0, 2.0, 3.0])

# [[1.0, 2.0], [3.0, 4.0]]의 2차원 텐서를 만들고 실수형 32비트로 지정
matrix = torch.tensor([[1.0, 2.0],
                       [3.0, 4.0]], dtype=torch.float32)

# matrix를 cpu에서 계산
matrix = matrix.to("cpu")

# 텐서 별 shape, dtype, device 출력
print("스칼라:", tuple(scalar.shape), scalar.dtype, scalar.device)
print("벡터:", tuple(vector.shape), vector.dtype, vector.device)
print("행렬:", tuple(matrix.shape), matrix.dtype, matrix.device)
print("행렬 값:", matrix.tolist())
