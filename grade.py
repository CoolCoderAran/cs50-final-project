import sys

def main():
    current_grades = input("Current Grades:")
    target_grade = input("Target Grade:")
    target_grade = float(target_grade)
    parsed_grades = parse_current_grades(current_grades)
    needed_grade = calculate_target_grade(parsed_grades, target_grade)
    grade = sum(parsed_grades) / len(parsed_grades)
    final_letter = final_letter_grade(grade)
    needed_grade = round(needed_grade)
    print(f"Your current grade is a {final_letter}.")
    print(f"In order to achieve your target grade, you need a {needed_grade} on your next assignment.")

def parse_current_grades(current_grades):
    try:
        parsed_grades = current_grades.split(",")
    except (AttributeError, ValueError, TypeError):
        sys.exit("There was an error.")
    else: return parsed_grades

def calculate_target_grade(parsed_grades, target_grade):

    needed_grade = target_grade*(len(parsed_grades)+1)- sum(parsed_grades)
    return needed_grade

def final_letter_grade(grade):
    if grade >= 90: final_letter = "A"
    elif grade >= 80: final_letter = "B"
    elif grade >= 70: final_letter = "C"
    elif grade >= 65: final_letter = "D"
    else: final_letter = "F"
    return final_letter

main()
