# 실습 05 · 범주형 결측과 미지 범주 변환 · 심화

PPT 46~54쪽 · 해당 교시 실습 25분 · 현재 폴더: `ex05_categorical/03_심화`

**아직 구현하지 않은 학생 코드의 실패는 정상입니다.** TODO 번호를 찾아 완성하세요.

## 목표
결측 표기 통일·전체 결측 계약·미지 범주 빈도 관찰을 구현한다.

## 입력과 사전 준비
`data/checkpoints/train.csv`·`valid.csv` 및 코드 안의 작은 배열
04~06의 고정 체크포인트는 전처리 전 자료입니다. 이전 실습 소스의 완성 여부와 무관하게 진행합니다.


## 구현 위치와 함수 계약
**`main.py::normalize_categories` — D5-05-H1**

문자열 공백 제거·소문자 변환, 빈 문자열/None/pd.NA는 np.nan으로 통일. 원본은 바꾸지 않고 index/columns를 보존한 object DataFrame을 반환합니다. 비문자·비결측 값은 ValueError를 발생시킵니다.

**`main.py::check_categorical_train` — D5-05-H2**

정규화 후 train 전체가 결측인 열이 있으면 이름을 담은 ValueError, 아니면 True.

**`main.py::unknown_counts` — D5-05-H3**

frame 각 열에서 학습 범주에 없고 결측도 아닌 값의 수를 dict로 반환. encoder를 다시 fit하지 않습니다. frame 열 순서는 fit 당시와 같습니다.


## 진행 순서
1. `학습기록.md`에 입력과 예상 결과를 먼저 적습니다.
2. 위 함수의 TODO를 구현합니다. 제공된 입출력·재사용 코드는 그대로 둡니다.
3. 실행하고 예상값과 실제값을 대조합니다. `expected_outputs` 파일을 읽어 정답을 복사하지 않습니다.
4. 자동 검사를 실행하고 실패 메시지의 함수/조건을 확인합니다.
5. 코드가 맞아도 판단 이유·시점·정책을 본인의 말로 설명합니다.

## 힌트
결측 표기 정리는 사전 결정한 행별 규칙이며 최빈값 학습과 다릅니다. 미지 범주 건수에는 결측을 넣지 마세요.

## 실행·검사 (현재 역할 폴더에서)
```text
python tools/run.py --exercise 05 --level advanced
python tools/check.py --exercise 05 --level advanced
```

가상환경을 활성화하지 않았다면 python 대신 `.venv`의 실행기 경로를 사용합니다.

## 완료 결과
`outputs/result.json` + 화면 출력 + `학습기록.md`

비교용: `expected_output.txt`와 `expected_outputs/result.json`
실습 07/08의 자동 검사는 통합된 이전 기능에도 의존합니다. 먼저 동일 난이도 07의 TODO를 완료하세요.

