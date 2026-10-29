from sklearn.preprocessing import OneHotEncoder

# 데이터 입력
train = [["qa"], ["summary"], ["qa"]]
valid = [["summary"], ["qa"]]

# 데이터 변환, 전처리
encoder = OneHotEncoder(sparse_output=False)
encoder.fit(train)
valid_ready = encoder.transform(valid).tolist()

# 열 순서, 변환값 출력
print("열 순서:", encoder.categories_[0].tolist())
print("valid 변환:", valid_ready)
