"""실습 01: 설치된 PyTorch와 CUDA 노출을 확인합니다. GPU가 없어도 CPU로 진행합니다."""
import torch

# pytorch, cuda 버전 및 사용 가능 여부 출력
print("PyTorch:", torch.__version__)
print("PyTorch CUDA 빌드:", torch.version.cuda)
print("CUDA 사용 가능:", torch.cuda.is_available())

# GPU 함수는 사용 가능한 경우에만 호출합니다. 드라이버 번호는 터미널 nvidia-smi에서 별도로 기록합니다.
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0)) # GPU 이름
    print("VRAM GiB:", round(torch.cuda.get_device_properties(0).total_memory / 1024**3, 2)) # GPU VRAM 용량
else:
    print("GPU: 이번 실행에서는 사용하지 않음")
print("이 단계의 연산 장치: cpu")

# 간단한 텐서 덧셈으로 검증
sample = torch.tensor([1.0, 2.0])
print("덧셈:", (sample + 1).tolist())
