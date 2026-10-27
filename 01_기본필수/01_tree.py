"""실습 01: 입력을 질문으로 나누는 트리를 만듭니다. 성능 평가가 아닌 원리 예제입니다."""
from sklearn.tree import DecisionTreeClassifier

# 데이터 입력
X = [[100], [200], [300], [700], [800], [900]]
y = [0, 0, 0, 1, 1, 1]  # 같은 순서의 정답: 성공 0, 실패 1

# X와 y로 model을 학습하고 250과 850을 예측합니다.
model = DecisionTreeClassifier(max_depth=1, random_state=42)
model.fit(X, y)
prediction = model.predict([[250], [850]])

# 예측값 출력
print("분기 기준:", model.tree_.threshold[0])
print("250·850 예측:", prediction.tolist())
