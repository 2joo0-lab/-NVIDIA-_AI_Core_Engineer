"""실습 04: 정상 숫자 두 열의 중요도를 확인하는 작은 원리 예제입니다."""
from sklearn.ensemble import RandomForestClassifier

# 데이터 입력
X = [[100, 1], [200, 2], [300, 1], [700, 2], [800, 1], [900, 2]]
y = [0, 0, 0, 1, 1, 1]
names = ["글자 수", "허용 도구 수"]

# 입력값 학습
model = RandomForestClassifier(n_estimators=20, max_depth=2, random_state=42, n_jobs=1)
model.fit(X, y)
importance = model.feature_importances_ # 학습한 model의 두 열이 예측에 얼마나 기여했는지 나타냄

# 결과 출력
for name, value in zip(names, importance):
    print(f"{name}: {value:.3f}")
print("중요도가 높아도 실패의 원인이라고 단정하지 않습니다.")
