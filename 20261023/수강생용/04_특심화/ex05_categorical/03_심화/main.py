"""Day5 실습 05 · 범주형 결측과 미지 범주 변환 · 심화."""
from pathlib import Path
import sys
import argparse
# 제공 코드: 역할 폴더 전체를 유지하면 현재 작업 폴더와 무관하게 실행할 수 있습니다.
ROLE_ROOT = Path(__file__).resolve().parents[2]
if str(ROLE_ROOT) not in sys.path:
    sys.path.insert(0, str(ROLE_ROOT))
from course_support import (DATA, NUM, CAT, FEATURES, FORBIDDEN, read_table,
                            load_raw, load_xy, load_dev, new_requests, emit)
import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

def normalize_categories(frame):
    """문자열 공백 제거·소문자 변환, 빈 문자열/None/pd.NA는 np.nan으로 통일.
    원본은 바꾸지 않고 index/columns를 보존한 object DataFrame을 반환합니다.
    비문자·비결측 값은 ValueError를 발생시킵니다.
    """
    # TODO D5-05-H1: 위 함수 설명의 입력·반환·검사 조건을 구현하세요.
    raise NotImplementedError("D5-05-H1를 완성하세요.")

def check_categorical_train(frame):
    """정규화 후 train 전체가 결측인 열이 있으면 이름을 담은 ValueError, 아니면 True."""
    # TODO D5-05-H2: 위 함수 설명의 입력·반환·검사 조건을 구현하세요.
    raise NotImplementedError("D5-05-H2를 완성하세요.")

def unknown_counts(encoder,frame):
    """frame 각 열에서 학습 범주에 없고 결측도 아닌 값의 수를 dict로 반환.
    encoder를 다시 fit하지 않습니다. frame 열 순서는 fit 당시와 같습니다.
    """
    # TODO D5-05-H3: 위 함수 설명의 입력·반환·검사 조건을 구현하세요.
    raise NotImplementedError("D5-05-H3를 완성하세요.")

def run():
    tr,va,_,_=load_dev(); train=normalize_categories(tr[CAT]); check_categorical_train(train)
    pipe=Pipeline([("imputer",SimpleImputer(strategy="most_frequent")),
        ("encoder",OneHotEncoder(handle_unknown="ignore",sparse_output=False))]).fit(train)
    messy=pd.DataFrame({"task_type":[" QA ","translation",None,"  "],
                        "priority":[" NORMAL ","urgent","",None]})
    normalized=normalize_categories(messy); transformed=pipe.transform(normalized)
    all_missing=pd.DataFrame({"task_type":[np.nan,np.nan],"priority":["low","high"]})
    try:
        check_categorical_train(all_missing)
    except ValueError:
        detected=True
    else:
        detected=False
    return {"normalized":normalized.to_dict(orient="list"),
            "unknown_counts":unknown_counts(pipe.named_steps["encoder"],normalized),
            "output_shape":list(transformed.shape),"all_missing_detected":detected}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "outputs")
    args = parser.parse_args()
    emit(run(), args.output)
