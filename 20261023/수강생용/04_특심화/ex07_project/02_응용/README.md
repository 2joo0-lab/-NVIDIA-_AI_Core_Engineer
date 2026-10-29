# 실습 07 · 전처리·분할 프로젝트 통합 · 응용

PPT 66~75쪽 · 해당 교시 실습 25분 · 현재 폴더: `ex07_project/02_응용`

**아직 구현하지 않은 학생 코드의 실패는 정상입니다.** TODO 번호를 찾아 완성하세요.

## 목표
저장/복원과 새 요청 계약 검사를 모듈에 연결한다.

## 입력과 사전 준비
`day5_ml/data/requests.csv`·`new_requests.csv`

07~08은 같은 프로젝트를 사용합니다. 08부터 실행하면 파일 없음 오류가 나므로 07부터 완성하세요.

## 구현 위치와 함수 계약
**`main.py::predict_new` — D5-07-A2**

입력 계약 검사 → 학습된 pre 변환 → predict, 정답 y 없이 수행합니다. 반환: (정규화한 입력, 변환 행렬, 예측 배열). 새 범주를 배우려고 재학습하지 않습니다.

**`provided_io.py::persist_and_verify` — D5-07-A1**

직접 생성한 Pipeline만 저장 직후 복원합니다. folder/pipeline.joblib에 dump 후 load. 예측뿐 아니라 변환 행렬·특성명도 대조합니다. 반환: restored_equal(bool), matrix_equal(bool), model_sha256(str) 사전. 외부에서 받은 joblib 파일은 이 함수에 넣지 않습니다.


## 진행 순서
1. `학습기록.md`에 입력과 예상 결과를 먼저 적습니다.
2. 위 함수의 TODO를 구현합니다. 제공된 입출력·재사용 코드는 그대로 둡니다.
3. 실행하고 예상값과 실제값을 대조합니다. `expected_outputs` 파일을 읽어 정답을 복사하지 않습니다.
4. 자동 검사를 실행하고 실패 메시지의 함수/조건을 확인합니다.
5. 코드가 맞아도 판단 이유·시점·정책을 본인의 말로 설명합니다.

## 힌트
실습 01~06의 재사용 코드와 입출력 보조 코드는 제공됩니다. 새 프로젝트를 다시 만들지 말고 같은 day5_ml을 08에서 검증하세요.

## 실행·검사 (현재 역할 폴더에서)
```text
python tools/run.py --exercise 07 --level applied
python tools/check.py --exercise 07 --level applied
```

가상환경을 활성화하지 않았다면 python 대신 `.venv`의 실행기 경로를 사용합니다.

## 완료 결과
`day5_ml/outputs`의 CSV·JSON·자체 생성 Pipeline + REPORT.md·TEST_LOG.md

비교용: `expected_output.txt`와 `expected_outputs`의 텍스트/CSV/JSON. 학습된 binary 모델은 각자가 생성합니다.
실습 07/08의 자동 검사는 통합된 이전 기능에도 의존합니다. 먼저 동일 난이도 07의 TODO를 완료하세요.

