# -*- coding: utf-8 -*-
# 2026-10-20 Day 2 | 실습 05 | 응용
# 유효 점수 필터와 수강생 요약 | PPT 54쪽
# 실행: python main.py (이 파일이 있는 폴더에서)
# 입력·완료 기준·예상 결과: 같은 폴더의 README.md, sample_input.txt, expected_output.txt
# 수강생용: TODO 부분을 완성한다. 제공된 입출력 형식과 함수 이름은 유지한다.
# NotImplementedError는 미완성 위치를 알리는 표식이다. 해당 줄을 실제 구현으로 교체한다.

def is_valid_score(score):
    """입력 계약: score는 int 또는 float인 점수이며 bool·문자열은 입력하지 않는다."""
    # TODO 01: 점수가 0~100 범위인지 bool로 반환하세요.
    return 0 <= score <= 100


def select_valid_scores(values):
    """유효 점수만 담은 새 List를 반환한다. 전달받은 List는 수정하지 않는다."""
    # TODO 02: 검사 함수를 호출해 유효 점수만 새 List에 담아 반환하세요.
    for score in values:
        if not is_valid_score(score):
            values.remove(score)
    return values


def summarize_student(student):
    """name·scores 키가 있는 Dict를 받아 유효 점수 통계를 문장으로 반환한다."""
    # TODO 03: 유효 점수 평균·개수·제외 개수를 반환하세요. 유효 점수가 없으면 별도 문장을 반환하세요.
    name = student["name"]
    scores = student["scores"]
    valid_scores = select_valid_scores(scores)
    valid_count = len(valid_scores)
    excluded_count = len(scores) - valid_count
    if valid_count > 0:
        average_score = sum(valid_scores) / valid_count
        return f"{name}: 평균 {average_score:.1f}, 유효 점수 {valid_count}개, 제외 {excluded_count}개"
    else:
        return f"{name}: 유효 점수가 없습니다. 제외 {excluded_count}개"


def main():
    students = [
        {"name": "민지", "scores": [80, 100, -1, 101]},
        {"name": "준호", "scores": [-5, 150]},
        {"name": "서연", "scores": []},
    ]
    for student in students:
        print(summarize_student(student))


if __name__ == "__main__":
    main()
