#스파르타 알고리즘 강의 3주차 해쉬 문제
# Q. 오늘 수업에 많은 학생들이 참여했습니다.
# 단 한 명의 학생을 제외하고는 모든 학생이 출석했습니다.
#
# 모든 학생의 이름이 담긴 배열과 출석한 학생들의 배열이 주어질 때,
# 출석하지 않은 학생의 이름을 반환하시오.

all_students = ["나연", "정연", "모모", "사나", "지효", "미나", "다현", "채영", "쯔위"]
present_students = ["정연", "모모", "채영", "쯔위", "사나", "나연", "미나", "다현"]


def get_absent_student(all_array, present_array):
    # 구현해보세요!
    _all = set(all_array)
    _present = set(present_array)
    absent = _all - _present
    return list(absent)

# 못품 강의 다시보기!!!!!!!!!!!!!!!!!!!!!

print(get_absent_student(all_students, present_students))