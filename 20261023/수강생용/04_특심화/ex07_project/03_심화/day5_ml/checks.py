"""입력·분할·학습 상태 검사. test 모델 평가는 수행하지 않습니다."""
import numpy as np
import pandas as pd

NUM=["input_chars","allowed_tools"]
CAT=["task_type","priority"]
FEATURES=NUM+CAT
FORBIDDEN={"request_id","failed","status","elapsed_ms","retry_count"}

def validate_features(frame, training=False, extra="error"):
    """입력 DataFrame을 계약에 맞게 검증하고 정규화한 복사본을 반환.
    1) 비어 있는 입력/중복 열/중복 index/누락 열/금지 열을 거부합니다.
    2) extra='drop'이면 일반 추가 열만 제외, extra='error'이면 오류입니다.
    3) NUM은 숫자/결측, 관측값은 유한·0 이상·정수 값이어야 합니다.
    4) CAT은 문자열/결측만 허용하고 strip/lower, 빈칸/None→np.nan을 적용합니다.
    5) training=True일 때 전체 결측 열은 명확한 오류. 추론의 결측은 허용합니다.
    """
    # TODO D5-07-H1: 위 함수 설명의 입력·반환·검사 조건을 구현하세요.
    raise NotImplementedError("D5-07-H1를 완성하세요.")

def check_splits(parts, all_ids):
    """세 부분 이름·내부 ID 고유성·X/y 순서·상호 독립·전체 포함을 검증.
    어떤 자료도 fit/transform/predict하지 않습니다. 실패하면 ValueError, 성공하면 True.
    """
    # TODO D5-07-H2: 위 함수 설명의 입력·반환·검사 조건을 구현하세요.
    raise NotImplementedError("D5-07-H2를 완성하세요.")

def snapshot(pre):
    """제공: fitted 학습 상태를 JSON 직렬화 가능한 독립 값으로 복사합니다."""
    num=pre.named_transformers_["num"]
    cat=pre.named_transformers_["cat"]
    return {"numeric_medians":num.named_steps["imputer"].statistics_.tolist(),
            "scaler_mean":num.named_steps["scaler"].mean_.tolist(),
            "scaler_scale":num.named_steps["scaler"].scale_.tolist(),
            "scaler_seen":int(num.named_steps["scaler"].n_samples_seen_),
            "categorical_modes":cat.named_steps["imputer"].statistics_.tolist(),
            "categories":[c.tolist() for c in cat.named_steps["encoder"].categories_],
            "feature_names":pre.get_feature_names_out().tolist()}

def assert_train_state(before,after,X_train):
    """상태가 변하지 않았고 NUM 중앙값이 train 값인지 확인, 실패하면 AssertionError.
    scaler가 본 행 수 역시 train 행 수와 같아야 합니다. 통계 출처와 불변을 함께 확인합니다.
    """
    # TODO D5-07-H3: 위 함수 설명의 입력·반환·검사 조건을 구현하세요.
    raise NotImplementedError("D5-07-H3를 완성하세요.")

def check_ready(train_ready,valid_ready,names):
    """제공: 행렬의 유한성, 열 수, 특성명 고유성과 금지 열 유입을 확인합니다."""
    if train_ready.ndim!=2 or valid_ready.ndim!=2:
        raise ValueError("전처리 출력은 2차원이어야 합니다.")
    if train_ready.shape[1]!=valid_ready.shape[1] or valid_ready.shape[1]!=len(names):
        raise ValueError("전처리 출력 열 수가 일치하지 않습니다.")
    if not np.isfinite(train_ready).all() or not np.isfinite(valid_ready).all():
        raise ValueError("전처리 출력에 NaN 또는 inf")
    if len(names)!=len(set(names)):
        raise ValueError("특성명 중복")
    for name in names:
        base=name.split("__",1)[-1]
        if any(base==bad or base.startswith(bad+"_") for bad in FORBIDDEN):
            raise ValueError(f"금지 특성명: {name}")
    return True
