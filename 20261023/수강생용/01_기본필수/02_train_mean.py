
# 데이터 입력
train_values = [10, 20]
valid_values = [100]

# 학습 데이터 평균과 전체 데이터 평균 비교
train_mean = sum(train_values) / len(train_values)
all_values = train_values + valid_values
all_mean = sum(all_values) / len(all_values)

# 평균값 출력
print("train 평균:", round(train_mean, 2))
print("전체 평균(비교만):", round(all_mean, 2))
print("실제 전처리에는 train 평균만 사용합니다.")
