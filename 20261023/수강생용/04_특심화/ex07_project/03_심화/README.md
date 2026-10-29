# 실습 07 · 전처리·분할 프로젝트 통합 · 심화

PPT 66~75쪽 · 해당 교시 실습 25분 · 현재 폴더: `ex07_project/03_심화`

**아직 구현하지 않은 학생 코드의 실패는 정상입니다.** TODO 번호를 찾아 완성하세요.

## 목표
입력·분할·학습 상태의 실패 조건을 자동 검사한다.

## 입력과 사전 준비
`day5_ml/data/requests.csv`·`new_requests.csv`

07~08은 같은 프로젝트를 사용합니다. 08부터 실행하면 파일 없음 오류가 나므로 07부터 완성하세요.

## 구현 위치와 함수 계약
**`checks.py::validate_features` — D5-07-H1**

입력 DataFrame을 계약에 맞게 검증하고 정규화한 복사본을 반환. 1) 비어 있는 입력/중복 열/중복 index/누락 열/금지 열을 거부합니다. 2) extra='drop'이면 일반 추가 열만 제외, extra='error'이면 오류입니다. 3) NUM은 숫자/결측, 관측값은 유한·0 이상·정수 값이어야 합니다. 4) CAT은 문자열/결측만 허용하고 strip/lower, 빈칸/None→np.nan을 적용합니다. 5) training=True일 때 전체 결측 열은 명확한 오류. 추론의 결측은 허용합니다.

**`checks.py::check_splits` — D5-07-H2**

세 부분 이름·내부 ID 고유성·X/y 순서·상호 독립·전체 포함을 검증. 어떤 자료도 fit/transform/predict하지 않습니다. 실패하면 ValueError, 성공하면 True.

**`checks.py::assert_train_state` — D5-07-H3**

상태가 변하지 않았고 NUM 중앙값이 train 값인지 확인, 실패하면 AssertionError. scaler가 본 행 수 역시 train 행 수와 같아야 합니다. 통계 출처와 불변을 함께 확인합니다.


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
python tools/run.py --exercise 07 --level advanced
python tools/check.py --exercise 07 --level advanced
```

가상환경을 활성화하지 않았다면 python 대신 `.venv`의 실행기 경로를 사용합니다.

## 완료 결과
`day5_ml/outputs`의 CSV·JSON·자체 생성 Pipeline + REPORT.md·TEST_LOG.md

비교용: `expected_output.txt`와 `expected_outputs`의 텍스트/CSV/JSON. 학습된 binary 모델은 각자가 생성합니다.
실습 07/08의 자동 검사는 통합된 이전 기능에도 의존합니다. 먼저 동일 난이도 07의 TODO를 완료하세요.

