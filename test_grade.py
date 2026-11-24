import pytest

from grade import parse_current_grades, calculate_target_grade, final_letter_grade

def test_parser():
    assert parse_current_grades(11.5, 12.5) == [11.5, 12.5]
    assert parse_current_grades(100, 90.2) == [100,90.2]



def test_checker():
    assert calculate_target_grade(100, 100) == 100



def test_letter():
    assert final_letter_grade(90) == "A""
    assert final_letter_grade(70) == "C"
    assert final_letter_grade(64) == "F""
