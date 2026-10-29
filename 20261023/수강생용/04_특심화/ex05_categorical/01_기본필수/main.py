"""Day5 실습 05 · 범주형 결측과 미지 범주 변환 · 기본필수."""
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

def fit_toy(train,valid):
    """범주형 train을 최빈값으로 채운 뒤 OneHotEncoder를 학습합니다.
    반환: imputer, encoder, valid_filled, valid_encoded.
    unknown은 ignore, sparse_output은 False. valid를 학습에 섞지 않습니다.
    """
    # TODO D5-05-B1: 위 함수 설명의 입력·반환·검사 조건을 구현하세요.
    raise NotImplementedError("D5-05-B1를 완성하세요.")

def run():
    train=np.array([["qa"],["research"],["qa"],[np.nan]],dtype=object)
    valid=np.array([[np.nan],["qa"],["summary"]],dtype=object)
    imp,enc,filled,ready=fit_toy(train,valid)
    return {"mode":imp.statistics_.tolist(),"categories":enc.categories_[0].tolist(),
            "valid_filled":filled.ravel().tolist(),"valid_encoded":ready.tolist()}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "outputs")
    args = parser.parse_args()
    emit(run(), args.output)
