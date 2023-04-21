def numerical_letter_grade(grades):
    

   
    letter_grade = []
    for gpa in grades:
        if gpa == 4.0:
            letter_grade.append("A+")
        elif gpa > 3.7:
            letter_grade.append("A")
        elif gpa > 3.3:
            letter_grade.append("A-")
        elif gpa > 3.0:
            letter_grade.append("B+")
        elif gpa > 2.7:
            letter_grade.append("B")
        elif gpa > 2.3:
            letter_grade.append("B-")
        elif gpa > 2.0:
            letter_grade.append("C+")
        elif gpa > 1.7:
            letter_grade.append("C")
        elif gpa > 1.3:
            letter_grade.append("C-")
        elif gpa > 1.0:
            letter_grade.append("D+")
        elif gpa > 0.7:
            letter_grade.append("D")
        elif gpa > 0.0:
            letter_grade.append("D-")
        else:
            letter_grade.append("E")
    return letter_grade

def test():
    assert (numerical_letter_grade([3.4, 3.7, 3.8, 3.4, 3.2, 3.7, 3.8, 3.7]) == 
    ['C-', 'A', 'A', 'A-', 'D-', 'B', 'B', 'B']), "failed test case"
    assert (numerical_letter_grade([0.0, 0.7, 0.8, 0.7, 0.0, 0.7, 0.8, 0.7]) == 
    ['E', 'E', 'D+', 'E', 'E', 'E', 'E', 'E']), "failed test case"
    print("All tests passed!")


test()
compare the outputs
