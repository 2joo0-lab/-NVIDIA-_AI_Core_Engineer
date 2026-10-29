"""Day5 실습 05 · 범주형 결측과 미지 범주 변환 · 응용."""
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

def make_categorical():
    """most_frequent 대체 → one-hot(ignore, dense)의 미학습 Pipeline 반환.
    단계 이름은 imputer, encoder입니다.
    """
    # TODO D5-05-A1: 위 함수 설명의 입력·반환·검사 조건을 구현하세요.
    raise NotImplementedError("D5-05-A1를 완성하세요.")

def run():
    Xtr,Xva,_,_=load_dev(); pipe=make_categorical()
    a=pipe.fit_transform(Xtr[CAT]); b=pipe.transform(Xva[CAT])
    categories=[c.copy() for c in pipe.named_steps["encoder"].categories_]
    probe=new_requests()[CAT]; unseen=pipe.transform(probe)
    return {"train_shape":list(a.shape),"valid_shape":list(b.shape),
            "modes":pipe.named_steps["imputer"].statistics_.tolist(),
            "categories":[c.tolist() for c in categories],"new_ready":unseen.tolist(),
            "new_shape":list(unseen.shape),
            "categories_unchanged":all(np.array_equal(a,b) for a,b in zip(categories,pipe.named_steps["encoder"].categories_))}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent / "outputs")
    args = parser.parse_args()
    emit(run(), args.output)
